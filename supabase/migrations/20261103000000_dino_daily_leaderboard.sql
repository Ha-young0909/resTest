-- 공룡 게임 일일 리더보드
-- 하루(한국 시간 기준)마다 새로 시작하고, 플레이어당 그날의 최고 점수 1건만 저장한다.

create table if not exists public.dino_scores (
  play_date   date        not null default ((now() at time zone 'Asia/Seoul')::date),
  player_name text        not null check (char_length(player_name) between 1 and 12),
  score       integer     not null check (score between 0 and 99999),
  updated_at  timestamptz not null default now(),
  primary key (play_date, player_name)
);

create index if not exists dino_scores_rank_idx
  on public.dino_scores (play_date, score desc, updated_at);

-- 테이블은 직접 읽고 쓰지 못하게 막고(정책 없음), 아래 함수로만 접근한다.
alter table public.dino_scores enable row level security;

-- 점수 제출: 오늘 기록보다 높을 때만 갱신한다. 반환값은 오늘의 최고 점수.
create or replace function public.submit_dino_score(p_name text, p_score integer)
returns integer
language plpgsql
security definer
set search_path = ''
as $$
declare
  v_name  text := btrim(coalesce(p_name, ''));
  v_today date := (now() at time zone 'Asia/Seoul')::date;
  v_best  integer;
begin
  if char_length(v_name) not between 1 and 12 then
    raise exception 'invalid player name';
  end if;
  if p_score is null or p_score not between 0 and 99999 then
    raise exception 'invalid score';
  end if;

  insert into public.dino_scores as s (play_date, player_name, score)
  values (v_today, v_name, p_score)
  on conflict (play_date, player_name) do update
    set score = excluded.score, updated_at = now()
    where excluded.score > s.score
  returning s.score into v_best;

  -- 갱신되지 않았다면(기존 점수가 더 높음) 기존 최고 점수를 돌려준다.
  if v_best is null then
    select s.score into v_best
    from public.dino_scores s
    where s.play_date = v_today and s.player_name = v_name;
  end if;

  return v_best;
end;
$$;

-- 오늘의 상위 N명 (동점이면 먼저 달성한 사람이 위).
create or replace function public.get_dino_daily_leaderboard(p_limit integer default 10)
returns table (rank bigint, player_name text, score integer)
language sql
stable
security definer
set search_path = ''
as $$
  select row_number() over (order by s.score desc, s.updated_at asc) as rank,
         s.player_name,
         s.score
  from public.dino_scores s
  where s.play_date = (now() at time zone 'Asia/Seoul')::date
  order by s.score desc, s.updated_at asc
  limit least(greatest(coalesce(p_limit, 10), 1), 50);
$$;

revoke all on function public.submit_dino_score(text, integer) from public;
revoke all on function public.get_dino_daily_leaderboard(integer) from public;
grant execute on function public.submit_dino_score(text, integer) to anon, authenticated;
grant execute on function public.get_dino_daily_leaderboard(integer) to anon, authenticated;

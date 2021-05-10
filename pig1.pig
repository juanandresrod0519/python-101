--Example-1
divs = LOAD '/user/hduser/ProgrammingPIG/NYSE_dividends' AS 
       (exchange, symbol, date, dividends);
--dump divs;
--Example-2
prices = LOAD '/user/hduser/ProgrammingPIG/NYSE_daily' as 
         (exchange, symbol, dateExc, open, high, low, 
          close, volume, adj_close);
ganancia1 = FOREACH prices GENERATE close - open;
ganancia2 = FOREACH prices GENERATE $6 - $3;
--dump ganancia1;
--dump ganancia2;
--Example-3
bgn = FOREACH prices GENERATE ..open;
middle = FOREACH prices GENERATE open..close;
end = FOREACH prices GENERATE volume..;
--DUMP end;
daily = LOAD '/user/hduser/ProgrammingPIG/NYSE_daily' AS 
         (exchange:chararray, symbol:chararray, 
          dateExc:chararray, open:float, high:float, 
          low:float, close:float, volume:int, 
          adj_close:float);
updown = FOREACH daily GENERATE symbol,$2,
                          daily.dateExc AS date,
			  (close>open?'UP':'DOWN');
--DUMP updown;
--Example-4
baseball = LOAD '/user/hduser/ProgrammingPIG/baseball' AS 
                (name:chararray, team:chararray, 
                 position:bag{t:(p:chararray)}, 
                 stats:map[]);
avg = FOREACH baseball GENERATE name, team, 
              stats#'batting_average' AS batting_avg;
avg_Report1 = FILTER avg BY (batting_avg IS NOT NULL);
--DUMP avg_Report1;
--Example-5
A1 = FOREACH baseball GENERATE position.p;
--DUMP A1;
baseballB = FOREACH baseball GENERATE {name, team};--bag
baseballM = FOREACH baseball 
            GENERATE [name, team] as Info;--map
baseballT = FOREACH baseball GENERATE (name, team);--tup
--DUMP baseballM;
newBaseballM1 = FOREACH baseballM GENERATE $0 AS Mariano;
newBaseballM2 = FOREACH newBaseballM1 GENERATE 
				      Mariano#'Mariano Rivera';
                                  
B = FILTER newBaseballM2 BY ($0 IS NOT NULL);
--DUMP B;
--Example-6
common_symbols = FILTER divs BY symbol IN ('CME','CTB','CHT');
--DUMP common_symbols; 
--Example-7
notMatching = FILTER divs BY NOT symbol MATCHES 'CM.*';
--DUMP notMatching; 
--Example-8
g = GROUP daily BY symbol;
cnt = FOREACH g GENERATE group, COUNT(daily);
--DUMP cnt;
cnt_Start = FOREACH g GENERATE group, COUNT_STAR(daily);
--DUMP cnt_Start;
cnt_Bag = FOREACH g GENERATE group, COUNT(daily.symbol);
--DUMP daily;
--DUMP cnt_Bag;
g_2k = GROUP daily BY (exchange, symbol);
avg_2k = FOREACH g_2k GENERATE group, 
                 AVG(daily.volume) AS AVG_VOLUME;
--DUMP avg_2k;
--Example-9
g_Team = GROUP baseball BY (team);
cnt_Teams = FOREACH g_Team 
            GENERATE group,COUNT(baseball.team);
--DUMP cnt_Teams;
--Example-10
baseball_lean = FOREACH baseball GENERATE name,
                                 FLATTEN(position) as pos;
g_byPosition = GROUP baseball_lean BY (pos);
cnt_byPosition = FOREACH g_byPosition
                GENERATE group, COUNT(baseball_lean.pos); 
--DUMP cnt_byPosition; 
--Example-11
baseball_lean_2 = FOREACH baseball GENERATE team, name,
                                   stats#'home_runs' AS hr;
baseball_lean_3 = FILTER baseball_lean_2 
                  BY (hr IS NOT NULL);
g_team_player = GROUP baseball_lean_3 BY (team, name);
cnt_HomeRuns = FOREACH g_team_player 
               GENERATE group, COUNT(baseball_lean_3);
--DUMP cnt_HomeRuns;
--Example-12
byDate = ORDER daily BY dateExc;
--DUMP byDate;
dailyDistinct = FOREACH daily GENERATE exchange,symbol;
unique = distinct dailyDistinct;
--DUMP unique;
--Example-13
jnd1= JOIN daily BY symbol, divs BY symbol;
--DUMP jnd1;
jnd2 = JOIN daily BY (symbol, dateExc), 
            divs BY (symbol, date);
--DUMP jnd2;
jndLeft = JOIN daily BY (symbol, dateExc) LEFT OUTER,
               divs BY (symbol, date);
filterjndLeft = FILTER jndLeft BY NOT daily::symbol
                                  MATCHES 'CM.*';
--DUMP filterjndLeft; 
frst10 = LIMIT divs 10;
--DUMP frst10;
frst10Percent = SAMPLE divs 0.15;
--DUMP frst10Percent;
--Example-14
grpd = COGROUP daily BY (exchange, symbol), divs BY (exchange,symbol);
sjnd = FILTER grpd BY NOT IsEmpty(divs);
fnl = FOREACH sjnd GENERATE FLATTEN(daily);
DUMP fnl;


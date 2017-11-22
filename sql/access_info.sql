SELECT OK.date, OK.num, ERROR.num
	FROM 
    (
        SELECT date(time) as date, count(*) as num
            FROM public.log
            WHERE status = '200 OK'
            GROUP BY status, date
            ORDER BY date ASC
    ) AS OK,
    (
        SELECT date(time) as date, count(*) as num
            FROM public.log
        	WHERE status = '404 NOT FOUND'
            GROUP BY status, date
            ORDER BY date ASC
    ) AS ERROR
    WHERE OK.date = ERROR.date
    GROUP BY OK.date, OK.num, ERROR.num
    ORDER BY OK.date ASC;
select aut.name, l.status, count(*) as num 
	from public.authors as aut, public.articles as art, public.log as l 
    where aut.id = art.author and l.path like '/article/%'||art.slug
	group by aut.name, l.status
    order by num desc;
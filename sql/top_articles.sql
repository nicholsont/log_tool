select art.title, count(*) as num 
	from public.authors as aut, public.articles as art, public.log as l 
    where aut.id = art.author and l.path like '/article/%'||art.slug
	group by art.title
    order by num desc;
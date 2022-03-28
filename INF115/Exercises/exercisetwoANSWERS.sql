insert into Game_info values ('League of fun', '2022', 'Noel Herrera', 'TenTenGames', 'MOBA', 'Danish');
update Game_info set Designer = 'Notch' where (Boardgame = 'League of fun' and Publisher = 'TenTenGames');

delete from Game_info where (Boardgame='Agricola' and Publisher ='Lookout Games');
alter table Game_sales drop foreign key Game_sales_ibfk_1; #Slette constraint key

alter table Game_info add constraint Year_Published check (Year_Published between 1980 and 2100);
alter table Game_info drop constraint Year_Published;

alter table Game_info add constraint Language check (Language in('English', 'Norwegian'));
alter table Game_info drop constraint Language;

show create table Game_sales; #Vise detaljene(brukt for å lete etter constraint key)


select * from Game_info;

#4b) This might be problematic because of the constraint keys. When language is constraited to English and Norwegian, we can't add the one with the German language.
import discord
from discord.ext import commands
import random
from cogs.utils import checks
uplay_accounts = ["Uplay Account by pk let's enjoy & invite your friends💛 -	davidbloechl@gmail.com:1e9022d95	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	gue.wesley@gmail.com:gernad1220	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	joaoluiz3d@hotmail.com:kakajoao	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	wolf9215@gmail.com:rasengan92	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	kyle_glen@hotmail.co.uk:kyleglen	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	payam758@gmail.com:killa963	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	endermenkiller3@gmail.com:herobrinehector5	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	bturney@gmail.com:ccsym243	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	hardys619@gmail.com:higrade1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	MadM4n617@gmail.com:mw3isbeast	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	demarco112778@aim.com:luvmike2	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	ddang31@hotmail.com:289373dhd	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	ralph.vanderweijde@gmail.com:rf614184	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	granthall@gmail.com:p4ssp0rt	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	philliepupy@gmail.com:gizzmo12	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	monkeydkakashi@hotmail.com:portgasdace	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	fuwad2009@gmail.com:passw0rd	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	nontagan555@hotmail.com:zigzag99	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	thebombes112@gmail.com:yourmom1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	farringtonstefan@gmail.com:yoda4ever	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	lbgga@yahoo.com.br:walker30	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	Thunair@seznam.cz:WX24uitr	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	gcsguti@hotmail.com:g81292006	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	deimarii@gmail.com:3inst3in	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	bandicoot_777@hotmail.com:4vth2htk	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	spkane00@gmail.com:was42abi	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	runemoellers@gmail.com:Juliane1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	bigshadow@gmail.com:sargas12	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	tjohnson5236@gmail.com:souledge0	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	russell.glorieux@gmail.com:year2121	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dangerdude203@gmail.com:Other203	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	wnchapin2010@yahoo.com:3047760w	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	wes.is.hxc@gmail.com:all4music	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	sjsankowski@gmail.com:lucymax1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	parodymaster117@gmail.com:zaktan117	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	lukaskonig24@yahoo.de:6gjfwzz9f	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dynamoteufel@yahoo.de:bmw30316	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	nickt911@att.net:babetesta	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	daloulou@hotmail.fr:acer5513	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	kellytj219@gmail.com:AstonVilla11	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	gaetan.caboche@laposte.net:gaetan78	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	cesar.klimkowicz@gmail.com:HEKTOR1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	amatsukuyom1@gmail.com:J04n37n47H	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	aurocs91@gmail.com:ignazio2	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	limited_boy@hotmail.co.uk:starwars3	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	niknitro24@gmail.com:NK201199	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	vanevery96@hotmail.com:linkinpark11	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	klokicoqwe@gmail.com:ico12345	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	delatorre_noe@yahoo.com:n21247oe	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	nathanizcool@hotmail.co.uk:Jasmine1234	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	damonjmiles@hotmail.com:david8555y	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	jacobvm@cox.net:secret123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	diantemadrid@gmail.com:xpd154dm	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	strelec.matyas@gmail.com:h3kfax0ee	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	bveracachay@gmail.com:tumama456	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	ssgtremy@gmail.com:corporal	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	fourcrafthun@gmail.com:rihegopa	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	herson.c.h@gmail.com:54839983he	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	robin.vandervegte@gmail.com:3uWudrad	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	korreca@gmail.com:alcantara	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	ottogiacomello@gmail.com:ottobotto	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	maurice.breure@gmail.com:welkom001	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	evansosiebo@gmail.com:anita123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	murryblackman@gmail.com:jyeran10	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	k2freestyle216@gmail.com:bl021690	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	tomsarnese@gmail.com:tas24ejb	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	twinky052@gmail.com:Werton007007	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dariuschernitsky@gmail.com:halo12and3	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	chance1callahan@gmail.com:cyb0rg32	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	underoath1617@gmail.com:bobbo0917	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	snowybell@gmail.com:razzlyw3n	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	gui.campello@hotmail.com:gui31999	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	spotsthedog@hotmail.com:buster345	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	idemers99@yahoo.com:soccer10	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	bu.43@live.com:beetle43	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	pvirgallito@gmail.com:spyder09	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	4ppleseed@gmail.com:counter7	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	rasmusdoej95@gmail.com:aga63dfd	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	tomamundsen@gmail.com:tack3toM	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	0310nik@gmail.com:0310nick	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	ciayinyan@hotmail.com:margarita89	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	smitttycent@gmail.com:488wilke	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	rajakty@gmail.com:6141ktty	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	stephen.machielse@hotmail.com:toegang21	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	starskils22@gmail.com:lichking2	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	stefan@oesie.de:Tischtennis89	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	lazark@live.com:australia5	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	tcpvtec@gmail.com:Makayla5198	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	Dizmog@gmail.com:nothingno1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	antoninweb@gmail.com:avionavi	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	eztenia@gmail.com:fatcat11	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	markyanchik@gmail.com:me123123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	Imobeous@yahoo.com:fuckall1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	vinckel@gmail.com:daimond8	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	shinygreenpally@gmail.com:deltaforce	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	MichaelAndersonSupreme@gmail.com:Herodude29	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	rafaelcorretor@gmail.com:surf2001	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	erdrick2k@gmail.com:mar13ino	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	jkpack1973@gmail.com:n1ntendo	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	nduffy86@gmail.com:lindsay04	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	ebrigstock@gmail.com:jagexer12	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	chris86_jaramillo@yahoo.com:blackops86	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	matuesz142@gmail.com:mateusz1999	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	rakasuki@gmail.com:Jennifer37	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	james.laudano@gmail.com:laudano87	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	rowen85@gmail.com:br0kend0wn	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	jenorocks@gmail.com:jenkins1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	emilianocesar@gmail.com:DNI29909433	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	torsten.voigt@gmail.com:torsten5	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	djlokster13@gmail.com:lambda100	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	usernamemadenchina@gmail.com:madeinchina1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	pikaboymc@gmail.com:pikaboy559	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	szucsjohn@gmail.com:koreajon69	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	kolyagaz@gmail.com:kolyagaz19951903	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	pdmckinley@gmail.com:safari505	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	spikytiger2001@gmail.com:nathaniel08	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dmd2689@gmail.com:diamond1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	paramanpl@gmail.com:niuniek36047	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	stusee@gmail.com:dharma1101	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	stohrster@gmail.com:WI19231	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	tankydog64@gmail.com:adminweb64	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	jmatney21@gmail.com:satansex123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	sergiota.cs@gmail.com:Sergio9898	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	mnewman784@gmail.com:matthewrules101	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	blackgod5300@gmail.com:cooow617	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	lairvus@gmail.com:1029qpwo38ei	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	swash018@gmail.com:wa00795267	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	chillystarcraft@gmail.com:Chillbeta15	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	hahaidontseeu@gmail.com:cyberlink	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	megamani.f@gmail.com:ryou0801	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	freitasmlucas@hotmail.com:lucas321	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	charleskassab1@hotmail.com:sefudeu45	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	pirao@uol.com.br:pirao9350	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	lucas_lucao@hotmail.com:klb10000	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	callahanr66@gmail.com:975310rcs	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	geovanebracale@hotmail.com:marcelochato	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	prego_shift@hotmail.com:prego123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	Zedemolay@gmail.com:digbi156	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	marcos_argello@hotmail.com:05tobias08	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	kyle.finlayson1997@gmail.com:1234green	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dst_alan@hotmail.com:alaneneu	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	donaug@hotmail.com:rapn1706	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dyegomatias@hotmail.com:ship2004	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	zpirslin@gmail.com:RockLee1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	rickroxrox@hotmail.com:zinaldo9	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	mariobros.brandao@hotmail.com:hepona123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	pieretti.henrique@gmail.com:shadow8563	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	divls-7@hotmail.com:1q2w3e4r	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	mbohac@bellsouth.net:flame123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	leandromarquesfernandes@hotmail.com:lmf553125	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	saulobborges@gmail.com:45dhfh50	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	haxel@live.se:Ah199622	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	joe.drye1@yahoo.com:hubcaps1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	fernandonegro666@hotmail.com:cone4567	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	kaiquevan@hotmail.com:kaique890100	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	bearpeidog@hotmail.com:cl0dh0pper	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	chaosmateus@hotmail.com:6ecf003f	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	deli_jak@hotmail.com:jeffhardy	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	jessejames1197@aol.com:candygolem1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	gabrielzs59@hotmail.com:zonasul59	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	ihonori0318@gmail.com:minmin12	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	siilenceex@gmail.com:wookieman55	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	hannes.aldrin@gmail.com:usbminne1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	rgvaldearg@gmail.com:Nhs20051	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	rubenx24@gmail.com:m4n0nth3run	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	solanin@gmail.com:stevevai1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	burner67@gmail.com:l1i9n8g3	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	eriksoc@gmail.com:hotmail1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	viniciusvilela19@gmail.com:leleu123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	joo--jope123@hotmail.com:megajoo210419933	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	firebox32@aol.com:ss9trunks	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	lucasbrumbaugh@comcast.net:green1380	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	rayng86@gmail.com:18125ray	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	petra.trnkova123@gmail.com:Gretien123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	hawkon003@hotmail.com:Chelsea2omfg	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	mait.mosona@gmail.com:Kolekoll007	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dougfour@gmail.com:troublein421	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	alskoja@seznam.cz:bobecekk	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	sammyboy709@yahoo.com:marty1992	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	adria.selva98@gmail.com:Adri131298	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	flipultraman@gmail.com:McWubstep	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dinaandrei219@yahoo.com:brasov56	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	apples_are_great@hotmail.co.uk:happyfeet1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dedwards1996@hotmail.com:mar1lynman5on	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	mmorpg.gp@gmail.com:Clickers007i17	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	szogun850@gmail.com:monika19810	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	johonybrohony@gmail.com:Krapfen1	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	alex.ghisoi@gmail.com:ilovebebe22	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	nomadking777@gmail.com:nomad747	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dkdkrmfjr@gmail.com:dla123wns	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	mb2222@gmail.com:077917AN	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	alcarazvizan@gmail.com:rose0juanita	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dog_dude_123@hotmail.com:bacon123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	mentalmatt88@yahoo.com:harrison78	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	etorres456@gmail.com:Riddick456	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	samuel.grabanica@gmail.com:Samuel123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	agony12@hotmail.com:cowboy4life	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	ben_south@hotmail.co.uk:isleofwight	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	dickboongan@yahoo.com:cidnag1818	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	henkka.jutila@hotmail.com:kuweeGe3	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	maco.jakub@gmail.com:maco123456	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	gabrielluis_mourao@hotmail.com:glmrgl123	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	matheusrog@hotmail.com:matheus260897	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	fesmv@hotmail.com:aqmse1234	",
"Uplay Account by pk let's enjoy & invite your friends💛 -	mauro_sonza@hotmail.com:020602aa	"]

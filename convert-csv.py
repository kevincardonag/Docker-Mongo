import csv  
import json  

try:

	# file output
	jsonfile = open('file.json', 'w')
	jsonfile.write("[")

    # csv register 2017
	csvfile_2017 = open('scopus2017.csv', 'r')
	fieldnames = ("Authors","Author(s) ID", "Title", "Year","Source title", "Cited by", "Link", "Abstract", "Author Keywords",  "Document Type", "Source")
	reader = csv.DictReader( csvfile_2017, fieldnames)

	count = 0
	for row in reader:
		if count >= 1:
			if count <= 850:
				json.dump(row, jsonfile)
				jsonfile.write(",")
				jsonfile.write("\n")
				count+=1
			else:
				break
		else:
			count+=1
			continue

	# csv register 2018
	csvfile_2018 = open('scopus2018.csv', 'r')
	fieldnames = ("Authors","Author(s) ID", "Title", "Year","Source title", "Cited by", "Link", "Abstract", "Author Keywords", "Index Keywords")
	reader = csv.DictReader( csvfile_2018, fieldnames)

	count = 0
	for row in reader:
		if count >= 1:
			if count <= 850:
				json.dump(row, jsonfile)
				jsonfile.write(",")
				jsonfile.write("\n")
				count+=1
			else:
				break
		else:
			count+=1
			continue

	# csv register 2019
	csvfile_2019 = open('scopus2019.csv', 'r')
	fieldnames = ("Authors","Author(s) ID", "Title", "Year","Source title", "Cited by", "Link", "Abstract", "Author Keywords",  "Document Type", "Source")
	reader = csv.DictReader( csvfile_2019, fieldnames)

	count = 0
	for row in reader:
		if count >= 1:
			if count <= 800:
				json.dump(row, jsonfile)
				jsonfile.write(",")
				jsonfile.write("\n")
				count+=1
			else:
				break
		else:
			count+=1
			continue

	jsonfile.write("]")

except Exception as Error:
	print(Error)


{
   "Authors": "Aguiar P.N., Jr, Roitberg F., Noia Barreto C.M., Adashek J.J., Del Giglio A., Lopes G.L., Jr",
   "Author(s) ID": "56779683600;57207346482;57191955820;57057669200;7004152210;57206206617;",
   "Title": "Back to the Future: In the Era of Cost-Effectiveness Analysis, Affordability Is a Limiting Factor for Patients’ Access to Innovative Cancer Treatments",
   "Year": 2019,
   "Source title": "Value in Health Regional Issues",
   "Cited by": null,
   "Link": "https://www.scopus.com/inward/record.uri?eid=2-s2.0-85062443556&doi=10.1016%2fj.vhri.2018.12.003&partnerID=40&md5=98c284afbd484e5a6eefc1c847d6f8b0",
   "Abstract": "Background: Over the past 5 years, 55 new anticancer drugs have been launched worldwide. Considering the increasing costs of innovative treatments, both the number and the relevance of cost-effectiveness analyses have increased, meaningfully supporting decision making by stakeholders and policy makers. Notably, cost-effective treatments remain unavailable to patients because they are still unaffordable for a multitude of payers. Objectives: To discuss the differences between cost effectiveness and affordability. Methods: We reviewed the most relevant data on the divergences between cost effectiveness and affordability. In addition, we included our recommendations to improve patients’ access to innovative cancer therapies. Results: The increasing costs of recently launched antineoplastic drugs, as high as $150 000 per year, represent a major barrier to patients’ access to treatments globally. In Brazil, for example, patients’ access to innovative treatments depends greatly on whether the individual has private health insurance. In the public health sector, patients’ access to cost-effective innovative treatments varies according to the financial capacity of the facility, leading to inequalities within the same healthcare system. Conclusions: We conclude that because of the socioeconomic inequality mostly seen in lower and middle-income countries, it is difficult to define a cost-effectiveness threshold by region or a willingness-to-pay threshold affordable to the entire population. We consider that benchmark interventions might help to find an affordable willingness-to-pay threshold, and league table interventions might help policy makers, physicians, and the society to share the decision making. © 2019 ISPOR–The professional society for health economics and outcomes research",
   "Author Keywords": "drug therapy; health policies; pharmacoeconomics",
   "Document Type": "Article",
   "Source": "Scopus"
 },

  {
   "Authors": "Matejcic M., Saunders E.J., Dadaev T., Brook M.N., Wang K., Sheng X., Olama A.A.A., Schumacher F.R., Ingles S.A., Govindasami K., Benlloch S., Berndt S.I., Albanes D., Koutros S., Muir K., Stevens V.L., Gapstur S.M., Tangen C.M., Batra J., Clements J., Gronberg H., Pashayan N., Schleutker J., Wolk A., West C., Mucci L., Kraft P., Cancel-Tassin G., Sorensen K.D., Maehle L., Grindedal E.M., Strom S.S., Neal D.E., Hamdy F.C., Donovan J.L., Travis R.C., Hamilton R.J., Rosenstein B., Lu Y.-J., Giles G.G., Kibel A.S., Vega A., Bensen J.T., Kogevinas M., Penney K.L., Park J.Y., Stanford J.L., Cybulski C., Nordestgaard B.G., Brenner H., Maier C., Kim J., Teixeira M.R., Neuhausen S.L., De Ruyck K., Razack A., Newcomb L.F., Lessel D., Kaneva R., Usmani N., Claessens F., Townsend P.A., Gago-Dominguez M., Roobol M.J., Menegaux F., Khaw K.-T., Cannon-Albright L.A., Pandha H., Thibodeau S.N., Schaid D.J., Henderson B.E., Stern M.C., Thwaites A., Guy M., Whitmore I., Morgan A., Fisher C., Hazel S., Livni N., Cook M., Fachal L., Weinstein S., Beane Freeman L.E., Hoover R.N., Machiela M.J., Lophatananon A., Carter B.D., Goodman P., Moya L., Srinivasan S., Kedda M.-A., Yeadon T., Eckert A., Eklund M., Cavalli-Bjoerkman C., Dunning A.M., Sipeky C., Hakansson N., Elliott R., Ranu H., Giovannucci E., Turman C., Hunter D.J., Cussenot O., Orntoft T.F., Lane A., Lewis S.J., Davis M., Key T.J., Brown P., Kulkarni G.S., Zlotta A.R., Fleshner N.E., Finelli A., Mao X., Marzec J., MacInnis R.J., Milne R., Hopper J.L., Aguado M., Bustamante M., Castaño-Vinyals G., Gracia-Lavedan E., Cecchini L., Stampfer M., Ma J., Sellers T.A., Geybels M.S., Park H., Zachariah B., Kolb S., Wokolorczyk D., Lubinski J., Kluzniak W., Nielsen S.F., Weisher M., Cuk K., Vogel W., Luedeke M., Logothetis C.J., Paulo P., Cardoso M., Maia S., Silva M.P., Steele L., Ding Y.C., De Meerleer G., De Langhe S., Thierens H., Lim J., Tan M.H., Ong A.T., Lin D.W., Kachakova D., Mitkova A., Mitev V., Parliament M., Jenster G., Bangma C., Schroder F.H., Truong T., Koudou Y.A., Michael A., Kierzek A., Karlsson A., Broms M., Wu H., Aukim-Hastie C., Tillmans L., Riska S., McDonnell S.K., Dearnaley D., Spurdle A., Gardiner R., Hayes V., Butler L., Taylor R., Papargiris M., Saunders P., Kujala P., Talala K., Taari K., Bentzen S., Hicks B., Vogt A., Hutchinson A., Cox A., George A., Toi A., Evans A., van der Kwast T.H., Imai T., Saito S., Zhao S.-C., Ren G., Zhang Y., Yu Y., Wu Y., Wu J., Zhou B., Pedersen J., Lobato-Busto R., Ruiz-Dominguez J.M., Mengual L., Alcaraz A., Pow-Sang J., Herkommer K., Vlahova A., Dikov T., Christova S., Carracedo A., Tretarre B., Rebillard X., Mulot C., Adolfsson J., Stattin P., Johansson J.-E., Martin R.M., Thompson I.M., Jr., Chambers S., Aitken J., Horvath L., Haynes A.-M., Tilley W., Risbridger G., Aly M., Nordström T., Pharoah P., Tammela T.L.J., Murtola T., Auvinen A., Burnet N., Barnett G., Andriole G., Klim A., Drake B.F., Borre M., Kerns S., Ostrer H., Zhang H.-W., Cao G., Lin J., Ling J., Li M., Feng N., Li J., He W., Guo X., Sun Z., Wang G., Guo J., Southey M.C., FitzGerald L.M., Marsden G., Gómez-Caamaño A., Carballo A., Peleteiro P., Calvo P., Szulkin R., Llorca J., Dierssen-Sotos T., Gomez-Acebo I., Lin H.-Y., Ostrander E.A., Bisbjerg R., Klarskov P., Røder M.A., Iversen P., Holleczek B., Stegmaier C., Schnoeller T., Bohnert P., John E.M., Ost P., Teo S.-H., Gamulin M., Kulis T., Kastelan Z., Slavov C., Popov E., Van den Broeck T., Joniau S., Larkin S., Castelao J.E., Martinez M.E., van Schaik R.H.N., Xu J., Lindstrӧm S., Riboli E., Berry C., Siddiq A., Canzian F., Kolonel L.N., Le Marchand L., Freedman M., Cenee S., Sanchez M., Wiklund F., Chanock S.J., Easton D.F., Eeles R.A., Kote-Jarai Z., Conti D.V., Haiman C.A., The PRACTICAL Consortium",
   "Author(s) ID": "54583939800;35183905800;42261371200;55920685000;57194604513;36939956100;23668431400;56563710100;7004611481;55211663700;41860918900;8551151700;7006558522;16301586800;57204744148;57201568161;7004025701;7003733464;57193235013;7202537971;34975062600;57204528351;6603885868;7005802145;57198881249;7003869478;57202560152;6602596107;57203230084;6602845723;10642045500;7102269363;35393852700;57205203609;55417996700;7006381597;7402615891;7102586287;57189528651;57193910834;7003579650;55883554800;6701643579;57204080924;6603267618;57202932188;7202266838;6603611727;7007170557;55173985500;8909099300;37106994900;57206483700;57205476591;9745962000;6604014355;6701318174;36141924300;57201889850;35318720900;56601682400;57205348123;57205429891;7004080206;57205054455;57202226578;57202033064;7003309232;34573421500;7006237594;57202562433;26636700200;57202458048;23667636400;57202457151;56645063900;7402131310;57192190481;20433920300;12446815900;35748306900;7202467316;8354328100;7202691823;57205131998;57204947356;57196837907;7102668993;55927746700;55163946300;6602695989;57200631349;56850062000;16033089900;57192201106;57203070588;57191514162;8626646800;57201816404;56276313000;57203069058;57202051628;56886847900;7005231497;57203052303;57204451579;57198811524;9739216100;57198175167;55454877800;57202451461;7005485439;7006135086;57203105051;55726774600;55968361800;6602519603;57202965119;57204698777;57205570240;10539367000;8696554500;54417240700;20733747900;57202277514;57199107445;35372999200;55356433400;57205482300;7004136104;7006083248;14422881300;57204947817;57202571213;57196395134;57202450707;55357785700;55536953600;23994382200;35406084500;55349129300;56362458200;55639493300;57129598000;7102165614;56482512300;6701809550;55234234600;7004723073;36646550200;57202457739;57202448535;7403692268;55886778600;36939351200;7005433220;57203053750;7004365261;57200557183;57190244611;57205313265;56128015700;7201653530;56091890200;57192199216;57192193167;57192417953;32067477400;23991658800;26768219100;57205479978;7004428943;57202570382;7102700541;7005075599;7202139763;56302117500;36123686100;55355408500;35069775800;56786191700;6701786592;35754239300;57204812610;55045961400;35381552100;7402563876;37090409400;7006870478;57198743258;57190677460;57190135570;57190839074;7403578576;13703177000;57202458431;12799087900;13906373900;57189077062;57189061467;57203182932;6504409670;15128088500;6602608521;56090234200;7005628389;6602923630;55887182400;12770907100;55285209400;7006062179;6603773230;6701549138;57201694764;7005859758;57203083443;7202425517;55689388800;7201696761;24586572000;7102168906;7201660596;7005049426;7006010915;7006464092;36727147100;55388432800;57200004434;55545861690;6504786301;56193451900;7003408391;8641770100;35356463700;10243052000;24176800100;7003854479;16230625300;7006342986;57201636797;7401709911;57202453787;57202450286;56896244900;7006553457;36067784800;36069348800;57202435219;57189066039;13309557800;55709453000;57203217213;57205555236;8628561700;30467730600;36848189600;37097782700;56108956900;23487044400;16935919000;6508260570;24402530600;56637279300;57204342971;55631851700;7004357180;24377148600;55359575200;18535786100;7004145329;40262537600;57202453423;57203217221;8589671800;57202559117;6506305418;16233463700;6602214162;7003907231;20434407600;56069427700;6602792294;7006665886;6602099919;7404593703;7003483971;57203521468;57205490970;57202566748;57202448259;12786841100;56221555400;7005665016;7006229986;56752951700;6602075745;57198806193;6603952223;57204091001;16471950000;57202594401;6602820947;7006606035;6701722861;",
   "Title": "Erratum to: Germline variation at 8q24 and prostate cancer risk in men of European ancestry (Nature Communications, (2018), 9, 1, (4616), 10.1038/s41467-018-06863-1)",
   "Year": 2019,
   "Source title": "Nature Communications",
   "Cited by": null,
   "Link": "https://www.scopus.com/inward/record.uri?eid=2-s2.0-85060158210&doi=10.1038%2fs41467-019-08293-z&partnerID=40&md5=86dd9a6faf011157b7e93b2733f9136a",
   "Abstract": "The original version of this Article contained an error in the spelling of the author Manuela Gago-Dominguez, which was incorrectly given as Manuela G. Dominguez. This has now been corrected in both the PDF and HTML versions of the Article. © 2019, The Author(s).",
   "Author Keywords": "",
   "Document Type": "Erratum",
   "Source": "Scopus"
 },
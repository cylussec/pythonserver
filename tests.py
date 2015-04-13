import unittest
import client
import server

class TestThreadedServerMethods(unittest.TestCase):
    def setUp(self):
        self.host = '127.0.0.1'
        self.port = 6000
        self.password = 'newton'
        csvfile = 'passwords.csv'
        self.cls = client.ThreadedExponentClient

    def test_invalid_password(self):
        test_client = self.cls(self.host, self.port, self.password)

        with self.assertRaises(RuntimeError):
            test_client._auth('aaaaaaaaaaaaaaa')

        del(test_client)


    #def test_overflow_value(self):
        #couldnt test... we get memory errors before we run out of space
        #pass

    def test_get_value(self):
        test_client = self.cls(self.host, self.port, self.password)
        test_client._auth(self.password)

        self.assertEqual(test_client.send(98), 1380878341261486750656911803252309726876604105686729638072729543243701479670593033211008001443536626310535980077544691196522513327846303307992442770355560270350429006522588433404602387992091295744)
        self.assertEqual(test_client.send(0), 0)
        self.assertEqual(test_client.send(1), 1)
        self.assertEqual(test_client.send(1000), 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

        del(test_client)

    def test_multiple_connections(self):
        test_client1 = self.cls(self.host, self.port, self.password)
        test_client2 = self.cls(self.host, self.port, self.password)
        test_client3 = self.cls(self.host, self.port, self.password)

        self.assertTrue(test_client1._auth('avogadro'))
        self.assertTrue(test_client2._auth('fibonacci'))
        self.assertTrue(test_client3._auth('einstein'))

        self.assertEqual(test_client1.send(5), 1575310296012319324513291747378469400384951950404760102055186335713328141458839156744579945431060229888195994511786213069330427413002989392865330853831691774503845391844008569858972827681453088121240438538641465560458751595854886552441353512178374812099580419835581744897530764594815164378140628101559685233590251196777553247860768688568409674792566895407018146237041830745172958234100872536784243830621148236004389762707390156989025060121977098999508471578524848228625804210017346470346334666612287781321177776612828748595972721896985365883765593838317491987663692171279028032155126674485723421542376870488516432834816903243076245468556759912165712846748826436178749324103257817419200945853037368220058268182964542408465629614430049055108571868935399802038602480318385562516492063149740005852077136436509939379914814893754260217631128849186231695172295977459983831843929077073426714910251792507771100906382495765232831381787607905324715188004579511034447517147987783147245680194821702900920050078364338454989514745663316659528180140174291674542549620279821556345575773167962865167617501593898888927300514983004615479029049178725248015507261122644050489572783058250023694586484744117704326749664679596197304561419352009239968204193812508805285390024054986117895823484475745412014112731164234361481929528046784114901922930636986558978800392307572382096107837370030726343684975715700389062739250830754317655336507006628054558338135647216237310651857421998846978487459004722021453802911086861954633946528990315767676928110453595108963394757696853746948404327437338568574348913331918618468242443866501996664018980477195790803792486067052346676428188403708187469717091910243284352433537996948115331083289279230834466844850290486313268785174886159942294919633398098523748711583211487350106152214727630646074601595150388254581407058878801688219807985974041208068433247575401940815683775209834860295878394882623613078926569298908551250660337847053653949397100730640866004017523905016504851911771181361797947939818161444481978635501013025672711337266257865194107729913520160434893697649475510947324655178230028105028993207264829628344814636885792288820759654583728513982279008598888323920518137020740798118494869239857650024522534401753143598203968171036983224719375554360057427981675122844450387914294476754609024867057381371086911065172840893231551275599289079642898160113953921986462286366610367343527719324534204477071193571190643142094900427297632223388862583251963099043317039374122746201629344577143558045140365201459207444712246795368502108578975447089233268885397062709854590261425013847322802359322783110611230474330001568012069908862915248097236775766751967676495944457532108238389291960309808495853642487329896864225063757700585527271795634722594586676170331949628499659995598993383097782239815372570357683499729095930671556989473880284774106327075924048623034875707636693890664359574187118294335693934075503862131070224010682185963413891691734952871457971079059392183901968066407976459933279089735889538760703674668995539190893720677269938641733323762802480596767037958617770614232490490405265387785067389397035764719166605886676196010653883378060803627974526233232614008548326631200635584276805992381288763940880438191076962731956611639643883798565620455601358179279995872286891579999931072973990366178331916873195589753148347018771283120687585440048970989752465764847191154969597371959359436846427099717401574354224648250834627289941663169606362665984262587884468903599232482043385356966214374635814830839573532274777177594794996526352030672499871425251027658660786985370000633732928420428577581783755382818769722915902055586078580675467725334892066372998850320087780370649506374247020924206987567041206390077367039077275581926614853347895020836334565386140037860698519924832897636142077410071744319048336933630701373841269188199708663887688250606914583591852647915288018668435190070425966852127109895474769464927353066096794264478265939156263599108358151764401330202692116161937538303565979050986271841587402422237767483634961298353203224549983810341212901709197732319606223385406022965617326791482678213996428996117984134464571438316090273331898112408729911043149540805785591146559454500675201416015625)
        self.assertEqual(test_client2.send(5), 84722490768344305825614360453430440875716600125921074682396063374736029993881964190734407958018516083870312308858859515619341130555426648970795727118518656169224654804841918917194170329976501773092583174317460104015586552800088685713020587479863527310251528195905025104544958412875239241413189143004981607659865507970073059327790343178371605508156627547651581758524955886287479618297935237120440391651487243272501486433046753253878537092688089192765435881707713369763146875530051562130610265529981065361196409608082643107868071374744507459163645530495407702183320598146800587755932730696731284010148814088136354653692996659323009948888741689053652588006057917473712582827855628688319457084411981727867866411978605520296834125764712740638790925265007181568447209983904474853221446755577928555717247028989510859589050574721508965879624451209265315342134463899125961948516306384828230011613331487985857988297461685863783416648793416737718330119884815159952010860887967253097485597287743407281490610460548682496458052435195535144504866198101117088590853469865103386233008921777253457700589447491670009516891265844311405996373730264426993826705457536107278304760003487071842752662818701930755446169524994645937432622104783854148969039798090552250021791393213538710111968911362254850030259092412801587899987699628407399023095349474495033498917534313114481105793268108298491856254229440189713808127859697549168773714823491374409550249872781650675303057972663606739632763540794158923373278308109331834570021754113097233518565505948227369923584190581526578797051082829952155543947718746301258494275730582926023761335222757595866508909087510765044574489407198729753090279180609493346216214721951777253784949673209428776810635379339853528005024683873739272335810003561758842349203190164197870502550909805419411225546268228122278216622625896627341459198302626401538734822013165314153351071577799331284430172652613449184433916353791769748138627754374240638822309612135692841806960100372458783401330436968007901441269900662927130770971090403464403827179894078791517091230125234858793254775452555667704240688472032943926777488389280469528368415610253870942622055297508162668012895201764530997781217781536198428972358215566620103327620157813091337335833632427824300451600739321039210086790605933178574119297850173525493183750101157863698300399446626315893394157734770459201179188227256978513641427447154450122116022782129273228077660948618165098478163767141808135054989601360709535199471655036515238053726722756382483098006190516680959388971390273747897354734288637277650036150982829465756233647706708396761031368350546570510970147340136543021324750116567951623448489203962784450183071730232444279640785253443234665280318734950062961332152923859806440659046892190636861109633861225962583430738347717996920531683177769428339305180740231680252167800318876189653271885788562850205162427946386322855985893224978003683448943546350433139524081149204062685672283729070575993333475520689817760667578776719821505705154203390266053491910358192118654481494213501561532623333269156758833584750270778464875549610233148772259814214698619740866469121049085330045435325470303745720369824478255035547039193866219562269076794658079988924305715150304071465027851866221726344521718478499856566712144076899261887155696083885908035245672984429607107477826437185414405102303014253671951279625552421804114696672415587476747151872429555006914563604518857650729249825219014420750133548397297746386042215022843389748408459857842892558565213181933757036786998407721849144150553591872045452166051583811009058231388810555715645787976974362246531591826642661409309446174827842793185924935484015764942185913102033864054097997830666907802151910623711060049672628603182156639171997917652770286091140929306571255989231666934118240900886644390406905153564984563405103584807847424437650911586932349883059117390926385134845647567689834086073502589537561994759254111111716946654417832213543438912473945650466302565154865606725858444887459039420562501323143156825297348580416773103968644671112453100760457068607993880505062341109952759564085715942606845981899882166034841238834287871691874554502755202284373629726694660387335472461306214454262515162696256074972794938162921485363656383445407906635788615828113956431359380326331686155216059232708067336011737233703345629290178801373523116574537620133189179207133135901439664265364013093504259648601714312111063892298403930369455066482661122669369110489537722079763185718345495867122678034574145597726136452003892942413283585041089068983905961848955474524287867929272763750542369219082164668663108258892300396257743855536769249665979693000333567705594331250276210840688933398873534316222173650956318620205878999972988581107406065655001507668452579156543756894391996735729834786817062052475402946757407532680214785932090770035343710197833380542994968635012980361445394776473531672330420970029877984485239126106165211278318241915167117383788894885870003699578614589763375486316653483975398361637794178336414178295310659074217552983049306347317675712464857643737372819195157310925278106035448197243525584081245039822600790303176011444427585050295499136782504333825209947307373335728051486818933014343775704747638578266850516594070346832752271855528157505244575331883321610966320089826918183959284651128615012801412632137143029305598163784681821678070829048969921135308553075165440082741933644458761522848509411255631391486903449050581104280830186691103835620784932098376914369580351488802843967759076218145043176195203798617660019440804985860168552120927654604523087064588077144818770682814790120833644273233843575375059795303668606695417826062133443155617900488429629851667633136399359021075250150815070447127427694228552581493410293669547312109929647075290992909370504261629542612984155116142028160771168494947851560407123458343270825867397156825135781337054107277978568891054106002412199005973017310105169589901160594586788306508996410170736088770504264670269170053858797652963136546588467336245138836681990853842716206618095098210621703638477109611637016285408216870051541658611084974771828202133402136844211445615236470960529760274722118078219954523157098231121875432796156989910102099372664203293572952046414617455294855082301051512032420149510424462020181579339827694940661261367578345305592764661616216967045961732611825668477347299986444348228552040744704857158251524078514717616543079263434591915986157488381221316834019056387875255225597508445864387309898467152409663727569118825269813606251925542389295666917848170470451278913407780805863483142949793848018203024797163588734542678041444375478813056185613356060989856522333264738043356623424399885317850661987577534979986648235071514049460446711154060920979401598863305163540065095180851423615753661020030656815537552433540081058165054108454195617576706604545266313160138649319087297720430953958466113906420811012546938068348130965257220228224666782203333067590964520424134307792920655519536909149312279746955032789939617611070294855532245791385814484122115291535048161419907995712352700522202298365513056435933822248787303397445136265691978149422372416418223681605549183990634606872199427642420920220496956000641446473553111857721871133813912200909841402318402148694818991197039177379357836729219016032933542755323828675441764549951574570658620783754420608257956592781677916355546315537265879847313288408995080602692367324819990929217203337875746343504673057721617855917612131635440602799902641657130424304554070740333110734470008266168288766602456534379188073270253890545040219979208761202421822763184063841297758315604363942234785149535101490217346690556708644076117751073415849932888008311082584731494819468647860067495569248054295445887572076468311616893222442073035681858536456447704087905933055913106135294382425392540908543546559687877986214843443744698832376105457342418958432972431182861328125)
        self.assertEqual(test_client3.send(5), 168592765351025210433682421477047156392331855379775433371296720247404488061288995756815958483306784288336260797847629275992673475511137405539826612648652305437047368083296247941477951326603697640030267313275157975819676307778548508590487874316045106630865908286032571706921461642220735818702976151113353108632566199102072689806955379090838226818987769877398234242959970942760176253082858982176019715158692260610957948516746833756564061292307595712694942678029738195527531184047329243212465089421460957981197800921031558063479100877867677308579838634997672957121121787863719654122834118966397109662627331400702718364097761337719993999459004145790269954427578418246934599163278299085434728575803339670293004830354329005776539876422685604285900413246002129586662178802029050178852878946890354460470409860078828068253994241525755205984774249814020005589200328704685858112455994238883910533196115526195376121657018357972992286258912442885055243278445708827404541372899210845233580768547298977797846456227857456712637418747959980951741675025847495537512233065897878170964877614925232754131266917943333664856757359662877353191063589654129445532938494390569874506793439684956511452734723593821813996966088501265358164288565817678796912575989316919130220513513225582302016919164618734954669898397604164575218181833944521132312378165679509179514081698818989370672793505007846350759068228151680683601017727700864998839346644337808488443049118094828794287587903321121026706181931655198692435084336036328457983729024561948949834865666301517644540810771009022372666751543736205605791743487648378045445718904267395905931689347069670723658770589528610651232545181754643832266702821535680646360533468912364127424320963783288288775398101835205519126359189512601713933161271334294274525366164122612688009367533438817095805297571305481349318742317390641401518232459877175741202778645276500219770341044434890879502165099747001336659286705183552268923373071526245422302298006576550085360417526103093186540821469296998342532957213563593683851261745691154806907312817649874577139462219024594233342072914770259957160664802718830656256374610949962480123613318988229072900326459952356548739697155692804226794395241526467090726196997560168514900935504494167529570957234352329059751124649544276979064085386163718512440479983245396722137872198677762469382087665114705295293967724187614130789001535520647313061967677150174863721367803959565590989630958910487036776117958765736739340751921906702201189849013295909101627300162382772384854079567273428905589642509147653543637758905927910283764305870863817185014545119353019672416922546341411687905059085334235610912069067834067862417154715350221841851463418570560903877674912009069340535424543399148338796218622199757980657784983469942221313822440824798360842236706963587779956309263654579199116346338329399228294555780269048329985178980620809925909032748937998982771941545088775365029434662091750579413950728338290258139327388541227221708494878022289155596444747101941015149368650811860051179913394101172298212050147609727557710352529306485738734920423516919388132057283904930973843248058050353746233901643827182365188417989113845096535156501208625131529743384786464593632428983455407507159223737463829234346521390774868699607571899098985046349489912463480200093655959490896782110329141858716239187581117377090254000459140131065961546873469983496999275566140106986572704123135433025877007677225497896607710379874874872892070218019776257254280188519173457809670369075706257827403332816143626142754247433990796448706022789261176193106624622784063506021933726478832585951801324790737262214003739625384249075928417964926068156348994224522487641543571388988255553592756658849199900528041335886535603950492467594793740654644493758383420166743994007606365680638198305532984652142382239176552933231492820416253872656311568695710661751703792904938136070856218111204604660424261521231659656149367986823302050693819270189224146188199929433006286680668579710961359555844948595430215245882453724056702682669826780445582026904352994320964512205079350667824333449682582348917556793690762176073332825260115802530985758414198971326565449983327882434127526185149557538190979929098780867987566095419835607798535067066342957372336528779041320004749973022403347807794561431282145301161210320818832048752941479213609097349991997720808073452504607515442735521401950624400811032644817791190445379272972689453067132723378749711889998286760198384485278808307707269136940774875379798968624463320742635536551525818980775649037031595281635712449853922906166191448330590604585644458456404166256282153298762248155112421847145196036023219628152691740297086653299629688262939453125)

        del(test_client1)
        del(test_client2)
        del(test_client3)

    def test_invalid_port(self):
        with self.assertRaises(OverflowError):
            test_client = self.cls(self.host, 9999999999, self.password)
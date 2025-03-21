from bs4 import BeautifulSoup

html = """ <!DOCTYPE html>
<html>
<head>
    <title>Job URLs</title>
</head>
<body>
<iframe src="Fetching URLs starting from result 0..." width="100%" height="500px"></iframe><br>
<iframe src="Fetching URLs starting from result 100..." width="100%" height="500px"></iframe><br>
<iframe src="Fetching URLs starting from result 200..." width="100%" height="500px"></iframe><br>
<iframe src="Fetching URLs starting from result 300..." width="100%" height="500px"></iframe><br>
<iframe src="Fetching URLs starting from result 400..." width="100%" height="500px"></iframe><br>
<iframe src="Fetching URLs starting from result 500..." width="100%" height="500px"></iframe><br>
<iframe src="Fetching URLs starting from result 600..." width="100%" height="500px"></iframe><br>
<iframe src="Fetching URLs starting from result 700..." width="100%" height="500px"></iframe><br>
<iframe src="Fetching URLs starting from result 800..." width="100%" height="500px"></iframe><br>
<iframe src="Fetching URLs starting from result 900..." width="100%" height="500px"></iframe><br>
<iframe src="http://chaklala.cantonment.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="http://dsclakkimarwat.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="http://dts.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="http://gba.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="http://pid.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="http://stfs.psf.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="http://www.ntrc.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://aari.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://abad.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://accounts.google.com/ServiceLogin%3Fcontinue%3Dhttps://www.google.com/search%253Fq%253Dsite:*.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://advocategeneral.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://agri.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://agripunjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://agripunjab.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://alw.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://anf.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://archives.sindhculture.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://auqaf.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://balochistanpolice.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://beoe.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://bepf.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://bos.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://bsip.bnip.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://car.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://careers.lcbda.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ccri.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://cim.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://clc.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://cmit.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://cooperation.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://cpec.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://cpwb.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://crs.agripunjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://dai.agripunjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://data.lhc.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://dcmalir.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://dgipr.kp.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://dgme.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://dhqlodhran.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://districtcourtnorthwaziristan.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://districtjudiciarymohmand.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://dol.kp.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ecac.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://epd.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://epza.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ext.agripunjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ffc.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://field.agripunjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://finance.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://food.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://fpc.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://fpsc.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://fwf.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://governorbalochistan.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://hed.ajk.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://hed.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://home.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://hrma.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://humanrights.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ibts.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://icd.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://industries.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://iph.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://istd.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://korangifisheries.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://kpcsw.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://kpra.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://kptevta.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://labour.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://lac.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://law.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://lgcd.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://lhr.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://lpgcl.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://minorityaffairs.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://mlc.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://mo.cppa.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://mofa.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://mohw.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://mpdd.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://nacta.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://narcon.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ncd.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://nlp.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ofwm.agripunjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ombudsperson.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ophrd.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pac.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pakistanhalalauthority.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pal.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://parb.agripunjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pbit.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pcmmdc.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pcpc.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pcrwr.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pdma.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://peeca.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://peima.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://peri.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://peshawarhcatd.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://peshawarhcmb.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pessi.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pfsa.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pg.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://phimc.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pims.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pja.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://plga.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pmbmc.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pnd.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pnd.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pndkp.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ppb.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ppdb.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ppdcl.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ppp.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://ppra.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://president.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://prisons.kp.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://prisons.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://prisons.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://prmsc.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://prosecution.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://prra.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://psda.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://psf.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pshdsouthpunjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pspu.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://punjabpolice.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pwd.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pwd.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://pwwf.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://qal.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://regulationswing.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://rtw.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://savings.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://sbfb.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://scda.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://schooleducation.southpunjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://schools.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://sed.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://sgacd.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://sgad.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://sindhhighcourt.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://skaa.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://smta.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://smu.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://soil.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://spd.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://sstsindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://swd.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://swd.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://tepa.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://test.sindhhec.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://test2.sindhhec.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqahmedpureast.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqarifwala.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqburewala.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqccw.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqchishtian.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqdka.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqgojra.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqisakhel.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqjampur.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqkmk.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqkotaddu.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqliqauatpur.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqmcn.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqnrp.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqsadiqabad.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqshj.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://thqtaunsa.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://universitiesboards.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://visitgilgitbaltistan.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://wasa.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://wdd.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://wdd.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://wpdgb.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://wrci.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://wsd.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://www.ecp.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://www.finance.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://www.fpsc.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://www.google.com/search?q%3Dsite:*.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://www.p3a.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://www.passco.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://www.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://www.wapda.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://zabpgpi.kp.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://zakat.punjab.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://zda.sindh.gov.pk/jobs" width="100%" height="500px"></iframe><br>
<iframe src="https://zud7.pitb.gov.pk/jobs" width="100%" height="500px"></iframe><br>
</body>
</html> """  # Replace this with your actual HTML content

soup = BeautifulSoup(html, "html.parser")

# Extract all URLs from iframe tags
urls = [iframe["src"] for iframe in soup.find_all("iframe")]

# Print extracted URLs
for url in urls:
    print(url)

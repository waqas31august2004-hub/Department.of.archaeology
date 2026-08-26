import weasyprint

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
    *, *::before, *::after {
        box-sizing: border-box;
    }
    @page {
        size: A4;
        margin: 20mm 15mm;
        background-color: #fcfbf9;
        @bottom-right {
            content: "Page " counter(page) " of " counter(pages);
            font-size: 8pt;
            color: #718096;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
        @bottom-left {
            content: "Taxila Archaeological Survey & Historical Guide";
            font-size: 8pt;
            color: #718096;
            font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        }
    }
    body {
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        color: #2c3e50;
        background-color: #fcfbf9;
        margin: 0;
        padding: 0;
        line-height: 1.5;
        font-size: 10pt;
    }
    .header-banner {
        background-color: #2b3a4a;
        color: #ffffff;
        margin: -20mm -15mm 20px -15mm;
        padding: 25px 20px 20px 20px;
        border-bottom: 4px solid #b79536;
    }
    .header-banner h1 {
        margin: 0 0 6px 0;
        font-size: 22pt;
        font-weight: 700;
        letter-spacing: 0.5px;
    }
    .header-banner p {
        margin: 0;
        font-size: 11pt;
        color: #dbe2ef;
        font-weight: 300;
    }
    .intro-text {
        font-size: 10.5pt;
        margin-bottom: 20px;
        color: #334155;
    }
    h2 {
        color: #2b3a4a;
        font-size: 13pt;
        border-left: 4px solid #b79536;
        padding-left: 8px;
        margin-top: 22px;
        margin-bottom: 10px;
        page-break-after: avoid;
    }
    .card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 4px;
        padding: 12px 15px;
        margin-bottom: 12px;
        page-break-inside: avoid;
        box-shadow: 0 1px 2px rgba(0,0,0,0.02);
    }
    .card h3 {
        color: #1e293b;
        font-size: 11pt;
        margin: 0 0 6px 0;
        font-weight: bold;
    }
    .grid-details {
        margin: 0;
        padding: 0;
        list-style: none;
    }
    .grid-details li {
        margin-bottom: 4px;
        font-size: 9.5pt;
    }
    .grid-details strong {
        color: #475569;
        display: inline-block;
        width: 85px;
    }
    .archaeologists-section {
        background-color: #edf2f7;
        border-left: 4px solid #4a5568;
        padding: 15px;
        margin-top: 25px;
        border-radius: 0 4px 4px 0;
        page-break-inside: avoid;
    }
    .archaeologists-section h2 {
        margin-top: 0;
        border-left: none;
        padding-left: 0;
        color: #2d3748;
    }
</style>
</head>
<body>

<div class="header-banner">
    <h1>Taxila Archaeological Sites</h1>
    <p>Detailed Catalog of Excavated Ruins, Locations, Dates, and Leading Archaeologists</p>
</div>

<div class="intro-text">
    Taxila, situated in the Rawalpindi district of Punjab, Pakistan, is a UNESCO World Heritage site of immense global importance. Acting as a historic crossroads between South, Central, and Western Asia, the complex contains ancient urban settlements, prehistoric layers, and Buddhist university-monastery complexes. Below is the full catalog of excavated sites.
</div>

<h2>1. The Three Ancient Capital Cities</h2>

<div class="card">
    <h3>Bhir Mound (The First City)</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Located directly across from the modern Taxila Museum site.</li>
        <li><strong>Period:</strong> 6th century BCE (Achaemenid Persian era) down to the 2nd century BCE.</li>
        <li><strong>Excavator:</strong> Extensively excavated by Sir John Marshall (with initial preliminary trenching by Sir Alexander Cunningham).</li>
        <li><strong>Significance:</strong> Represents the earliest urban layout of Taxila, featuring irregular street patterns and rich early settlement artifacts.</li>
    </ul>
</div>

<div class="card">
    <h3>Sirkap (The Second City)</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Situated on the opposite side of the Tamra Stream from Bhir Mound.</li>
        <li><strong>Period:</strong> 2nd century BCE through the Greco-Bactrian, Indo-Scythian, and Indo-Parthian eras.</li>
        <li><strong>Excavator:</strong> Systematically excavated by Sir John Marshall over a multi-year campaign starting in 1913.</li>
        <li><strong>Significance:</strong> Famous for its formal Greek grid-iron city plan, defensive walls, palace complexes, and diverse shrines.</li>
    </ul>
</div>

<div class="card">
    <h3>Sirsukh (The Third City)</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Located further up the valley, northeast of Sirkap along the ancient tracks.</li>
        <li><strong>Period:</strong> 1st to 2nd century CE (Established under the Kushan Empire).</li>
        <li><strong>Excavator:</strong> Investigated and excavated by Sir John Marshall and Archaeological Survey of India teams.</li>
        <li><strong>Significance:</strong> Characterized by massive defensive stone walls with semicircular arrow-slit bastions built for defense against nomads.</li>
    </ul>
</div>

<h2>2. Prehistoric & Early Settlement Sites</h2>

<div class="card">
    <h3>Sarai Khola (Saraikala)</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Approximately 3 km southwest of the main Taxila museum complex.</li>
        <li><strong>Period:</strong> Neolithic and Early Bronze Age layers dating back prior to 3300 BCE.</li>
        <li><strong>Excavator:</strong> Excavated by Dr. Ahmad Hasan Dani (University of Peshawar) during the 1960s.</li>
        <li><strong>Significance:</strong> Uncovered deep prehistoric roots proving settled farming and proto-urban communities prior to historic kingdoms.</li>
    </ul>
</div>

<div class="card">
    <h3>Hatial Area</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Central ridge system near the urban settlement core.</li>
        <li><strong>Period:</strong> Early Iron Age and pre-urban settlement strata (c. 2550–2000+ BCE).</li>
        <li><strong>Excavator:</strong> Excavated by Bahadur Khan Chandio and Dr. Ashraf Khan (Pakistan Department of Archaeology).</li>
    </ul>
</div>

<div class="card">
    <h3>Khanpur Cave</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Khanpur valley corridor near Taxila.</li>
        <li><strong>Period:</strong> Mesolithic period.</li>
        <li><strong>Excavator:</strong> Documented and tested by national archaeological survey teams.</li>
    </ul>
</div>

<h2>3. Major Buddhist Stupas, Monasteries & Religious Complexes</h2>

<div class="card">
    <h3>Dharmarajika Stupa</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Roughly 3 km east of the Taxila Museum.</li>
        <li><strong>Period:</strong> 3rd century BCE (Maurya Period / Ashoka) expanded up to the 5th century CE.</li>
        <li><strong>Excavator:</strong> Excavated by Sir John Marshall between 1912 and 1916.</li>
        <li><strong>Significance:</strong> The principal Buddhist sanctuary at Taxila built to enshrine sacred relics of the Buddha.</li>
    </ul>
</div>

<div class="card">
    <h3>Jaulian Monastery</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Perched high on a hill settlement about 1 mile east of Sirsukh.</li>
        <li><strong>Period:</strong> 2nd to 5th century CE (destroyed by White Huns around 450-460 CE).</li>
        <li><strong>Excavator:</strong> Excavated by Sir John Marshall and Mr. N. G. Majumdar in 1916–1917.</li>
        <li><strong>Significance:</strong> Exceptionally preserved university-monastery complex featuring intact stucco statues and relic caskets.</li>
    </ul>
</div>

<div class="card">
    <h3>Mohra Moradu</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Tucked into a peaceful valley pocket roughly 2 miles from Jaulian.</li>
        <li><strong>Period:</strong> Kushan to late Gupta periods (2nd–5th century CE).</li>
        <li><strong>Excavator:</strong> Excavated by Sir John Marshall and Shromani Ram in 1914–1915.</li>
        <li><strong>Significance:</strong> Celebrated for its pristine stucco stupa imagery and monastic assembly halls.</li>
    </ul>
</div>

<div class="card">
    <h3>Kunala Stupa & Monastery</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Built on a high ridge immediately south-southeast overlooking the Sirkap ruins.</li>
        <li><strong>Period:</strong> 2nd to 4th century CE (Kushan era).</li>
        <li><strong>Excavator:</strong> Excavated by Sir John Marshall.</li>
    </ul>
</div>

<div class="card">
    <h3>Kalawan</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Situated in the valley ravines branching toward the Margalla hills.</li>
        <li><strong>Period:</strong> 1st to 5th century CE.</li>
        <li><strong>Excavator:</strong> Excavated by Sir John Marshall and ASI teams during the 1920s.</li>
    </ul>
</div>

<div class="card">
    <h3>Pippala Monastery</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Hillside complex north of Sirsukh.</li>
        <li><strong>Period:</strong> Kushan through Hunnic destruction phases.</li>
        <li><strong>Excavator:</strong> Excavated by Sir John Marshall.</li>
    </ul>
</div>

<div class="card">
    <h3>Bhallar Stupa</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Easternmost spur of the Haro River hills, overlooking the valley.</li>
        <li><strong>Period:</strong> 2nd to 5th century CE.</li>
        <li><strong>Excavator:</strong> Excavated by Sir John Marshall / ASI staff.</li>
    </ul>
</div>

<div class="card">
    <h3>Bhamala Stupa</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Northern edge of the Taxila valley near the Haro riverbed.</li>
        <li><strong>Period:</strong> 4th to 5th century CE (Late Kushan / Kidarite period).</li>
        <li><strong>Excavator:</strong> Originally noted in early surveys and later thoroughly re-excavated by Dr. Mohammad Bahadur Khan.</li>
        <li><strong>Significance:</strong> Famous for discovery of a massive, rare reclining Buddha statue.</li>
    </ul>
</div>

<h2>4. Temples, Fortresses & Regional Outliers</h2>

<div class="card">
    <h3>Jandial Temple</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Located just north-northeast of the Sirkap city walls.</li>
        <li><strong>Period:</strong> 2nd century BCE (Indo-Greek or Parthian period).</li>
        <li><strong>Excavator:</strong> Excavated by Sir John Marshall.</li>
        <li><strong>Significance:</strong> Displays unique classical Greek Ionic column architecture, likely utilized as a Zoroastrian fire temple.</li>
    </ul>
</div>

<div class="card">
    <h3>Giri Complex (Giri Fort & Monasteries)</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Tucked deep in a defensive glen in the hills roughly 5 km from Dharmarajika.</li>
        <li><strong>Period:</strong> Spans both the Buddhist era (2nd–5th century CE) and a medieval Islamic fortified phase.</li>
        <li><strong>Excavator:</strong> Sir John Marshall and subsequent Pakistani departments.</li>
    </ul>
</div>

<div class="card">
    <h3>Lalchak & Badalpur</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Eastern valley peripheries.</li>
        <li><strong>Period:</strong> Kushan / Late Buddhist period.</li>
        <li><strong>Excavator:</strong> Surveyed and test-excavated by ASI and national archaeological teams.</li>
    </ul>
</div>

<div class="card">
    <h3>Tofkian & Bajran</h3>
    <ul class="grid-details">
        <li><strong>Location:</strong> Peripheral hill sectors surrounding the core valley.</li>
        <li><strong>Period:</strong> Contemporary Gandhara settlement periods.</li>
        <li><strong>Excavator:</strong> Mapped and documented during 20th-century valley surveys.</li>
    </ul>
</div>

<div class="archaeologists-section">
    <h2>Principal Figures in Taxila's Excavation History</h2>
    <ul class="grid-details" style="padding-left: 0;">
        <li><strong>Sir Alexander Cunningham:</strong> Founder of the Archaeological Survey of India who first identified and mapped the ruins of Taxila in the mid-19th century (1863–64 and 1872–73).</li>
        <li><strong>Sir John Marshall:</strong> Director-General of the ASI whose 20-year systematic excavation campaign (1913–1934) uncovered the vast majority of Taxila's monuments, ancient cities, and monasteries.</li>
        <li><strong>Dr. Ahmad Hasan Dani & Pakistani Archaeologists:</strong> Continued subsequent stratigraphical research (such as Sarai Khola) and preservation works post-independence.</li>
    </ul>
</div>

</body>
</html>
"""

with open("taxila_comprehensive_guide.html", "w", encoding="utf-8") as f:
    f.write(html_content)

weasyprint.HTML("taxila_comprehensive_guide.html").write_pdf("taxila_comprehensive_guide.pdf")
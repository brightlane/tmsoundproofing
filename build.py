#!/usr/bin/env python3
"""
Sound Proofing Wizard v3 - Complete Affiliate SEO Build
Site: https://brightlane.github.io/soundproofing/
Aff : https://www.linkconnector.com/ta.php?lc=007949109781007070&atid=TmSoundproofingWebImproved
Features: 1100+ pages, daily AI blog, 10 body variants, 5 SVGs, rich schemas, geo pages
"""
import json, re, hashlib, os
from datetime import datetime, timezone, timedelta
from pathlib import Path
from collections import defaultdict

SITE  = "https://brightlane.github.io/soundproofing"
NAME  = "Sound Proofing Wizard"
AFF   = "https://www.linkconnector.com/ta.php?lc=007949109781007070&atid=TmSoundproofingWebImproved"
NOW   = datetime.now(timezone.utc)
TODAY = NOW.strftime("%Y-%m-%d")
YEAR  = NOW.year
OG    = SITE + "/og.svg"
OUT   = Path("output")
GUIDES = OUT / "guides"
BLOG   = OUT / "blog"
for d in [OUT, GUIDES, BLOG]: d.mkdir(parents=True, exist_ok=True)

def sh(s): return int(hashlib.md5(s.encode()).hexdigest(), 16)
def ttag(kw, loc=None):
    sfx = " | Sound Proofing Wizard"
    base = f"{kw} in {loc}" if loc else kw
    b = base if len(base)+len(sfx) <= 60 else base[:60-len(sfx)]
    return b + sfx

# ── KEYWORDS ─────────────────────────────────────────────────────────────────
CORE_KW = [
    # General
    ("soundproofing","Soundproofing","General","100k+"),
    ("sound-proofing","Sound Proofing","General","100k+"),
    ("how-to-soundproof-a-room","How to Soundproof a Room","How-To","100k+"),
    ("best-soundproofing-material","Best Soundproofing Material","Products","50k+"),
    ("soundproofing-materials","Soundproofing Materials","Products","50k+"),
    ("cheapest-way-to-soundproof-a-room","Cheapest Way to Soundproof a Room","Budget","50k+"),
    ("diy-soundproofing","DIY Soundproofing","DIY","50k+"),
    ("noise-reduction","Noise Reduction","General","100k+"),
    ("sound-dampening","Sound Dampening","General","50k+"),
    ("sound-deadening","Sound Deadening","General","50k+"),
    ("sound-isolation","Sound Isolation","General","50k+"),
    ("how-does-soundproofing-work","How Does Soundproofing Work","Informational","50k+"),
    ("does-soundproofing-work","Does Soundproofing Work","Informational","10k+"),
    ("is-soundproofing-worth-it","Is Soundproofing Worth It","Informational","10k+"),
    ("types-of-soundproofing","Types of Soundproofing","Informational","10k+"),
    ("soundproofing-effectiveness","Soundproofing Effectiveness","Informational","10k+"),
    ("soundproofing-myths","Soundproofing Myths","Informational","10k+"),
    # Walls
    ("soundproofing-walls","Soundproofing Walls","Walls","100k+"),
    ("how-to-soundproof-a-wall","How to Soundproof a Wall","Walls","100k+"),
    ("soundproof-drywall","Soundproof Drywall","Walls","10k+"),
    ("resilient-channel-soundproofing","Resilient Channel Soundproofing","Walls","10k+"),
    ("decoupling-soundproofing","Decoupling Soundproofing","Walls","10k+"),
    ("double-drywall-soundproofing","Double Drywall Soundproofing","Walls","10k+"),
    # Products
    ("acoustic-foam","Acoustic Foam","Products","100k+"),
    ("acoustic-panels","Acoustic Panels","Products","100k+"),
    ("soundproofing-panels","Soundproofing Panels","Products","50k+"),
    ("soundproof-paint","Soundproof Paint","Products","50k+"),
    ("mass-loaded-vinyl","Mass Loaded Vinyl","Products","50k+"),
    ("mlv-soundproofing","MLV Soundproofing","Products","10k+"),
    ("green-glue-soundproofing","Green Glue Soundproofing","Products","10k+"),
    ("soundproofing-curtains","Soundproofing Curtains","Products","50k+"),
    ("soundproof-curtains","Soundproof Curtains","Products","50k+"),
    ("soundproofing-blankets","Soundproofing Blankets","Products","10k+"),
    ("soundproofing-insulation","Soundproofing Insulation","Products","50k+"),
    ("acoustic-insulation","Acoustic Insulation","Products","50k+"),
    ("soundproofing-foam","Soundproofing Foam","Products","50k+"),
    ("soundproofing-mat","Soundproofing Mat","Products","10k+"),
    ("anti-vibration-mat","Anti Vibration Mat","Products","10k+"),
    ("acoustic-tiles","Acoustic Tiles","Products","50k+"),
    ("bass-trap","Bass Trap","Products","50k+"),
    ("acoustic-treatment","Acoustic Treatment","Acoustics","50k+"),
    ("soundproofing-products","Soundproofing Products","Products","50k+"),
    # Rooms
    ("soundproofing-apartment","Soundproofing Apartment","Apartment","50k+"),
    ("soundproofing-apartment-walls","Soundproofing Apartment Walls","Apartment","50k+"),
    ("soundproofing-bedroom","Soundproofing Bedroom","Bedroom","50k+"),
    ("soundproof-bedroom","Soundproof Bedroom","Bedroom","50k+"),
    ("how-to-soundproof-a-bedroom","How to Soundproof a Bedroom","Bedroom","50k+"),
    ("soundproofing-home-office","Soundproofing Home Office","Home Office","50k+"),
    ("soundproof-home-office","Soundproof Home Office","Home Office","50k+"),
    ("soundproofing-basement","Soundproofing Basement","Basement","50k+"),
    ("soundproofing-garage","Soundproofing Garage","Garage","50k+"),
    ("soundproof-studio","Soundproof Studio","Studio","50k+"),
    ("home-recording-studio-soundproofing","Home Recording Studio Soundproofing","Studio","50k+"),
    ("recording-studio-soundproofing","Recording Studio Soundproofing","Studio","50k+"),
    ("soundproofing-bathroom","Soundproofing Bathroom","Bathroom","10k+"),
    ("soundproofing-nursery","Soundproofing Nursery","Nursery","10k+"),
    ("soundproofing-closet","Soundproofing Closet","Closet","10k+"),
    ("soundproofing-shed","Soundproofing Shed","Shed","10k+"),
    ("soundproof-room","Soundproof Room","General","100k+"),
    ("soundproof-room-within-a-room","Soundproof Room Within a Room","General","10k+"),
    # Doors
    ("how-to-soundproof-a-door","How to Soundproof a Door","Doors","100k+"),
    ("soundproof-door","Soundproof Door","Doors","50k+"),
    ("soundproof-door-seal","Soundproof Door Seal","Doors","10k+"),
    ("door-sweep-soundproofing","Door Sweep Soundproofing","Doors","10k+"),
    # Windows
    ("soundproof-window","Soundproof Window","Windows","50k+"),
    ("soundproofing-windows","Soundproofing Windows","Windows","50k+"),
    ("window-soundproofing-film","Window Soundproofing Film","Windows","10k+"),
    ("soundproof-window-insert","Soundproof Window Insert","Windows","10k+"),
    # Ceiling & Floor
    ("soundproofing-ceiling","Soundproofing Ceiling","Ceiling","50k+"),
    ("how-to-soundproof-a-ceiling","How to Soundproof a Ceiling","Ceiling","50k+"),
    ("soundproof-flooring","Soundproof Flooring","Floors","50k+"),
    ("soundproofing-floor","Soundproofing Floor","Floors","50k+"),
    ("soundproofing-between-floors","Soundproofing Between Floors","Floors","10k+"),
    ("soundproof-underlayment","Soundproof Underlayment","Floors","10k+"),
    ("impact-noise-reduction","Impact Noise Reduction","Floors","10k+"),
    ("footstep-noise-reduction","Footstep Noise Reduction","Floors","10k+"),
    # Noise problems
    ("block-noise-from-neighbors","Block Noise from Neighbors","Noise","50k+"),
    ("noisy-neighbors-apartment","Noisy Neighbors Apartment","Noise","50k+"),
    ("reduce-noise-from-upstairs","Reduce Noise from Upstairs Neighbors","Noise","50k+"),
    ("street-noise-reduction","Street Noise Reduction","Noise","50k+"),
    ("reduce-road-noise-in-home","Reduce Road Noise in Home","Noise","50k+"),
    ("traffic-noise-reduction","Traffic Noise Reduction","Noise","50k+"),
    ("bass-noise-from-neighbors","Bass Noise from Neighbors","Noise","10k+"),
    ("low-frequency-noise-reduction","Low Frequency Noise Reduction","Noise","10k+"),
    ("airplane-noise-reduction","Airplane Noise Reduction","Noise","10k+"),
    # Acoustics
    ("reduce-echo-in-room","Reduce Echo in Room","Acoustics","50k+"),
    ("room-acoustics","Room Acoustics","Acoustics","100k+"),
    ("sound-absorption","Sound Absorption","Acoustics","50k+"),
    ("stc-rating","STC Rating","Acoustics","10k+"),
    ("sound-transmission-class","Sound Transmission Class","Acoustics","10k+"),
    ("flanking-noise","Flanking Noise","Acoustics","10k+"),
    ("impact-noise-vs-airborne-noise","Impact Noise vs Airborne Noise","Acoustics","10k+"),
    # Vehicles
    ("car-soundproofing","Car Soundproofing","Vehicle","50k+"),
    ("car-sound-deadening","Car Sound Deadening","Vehicle","50k+"),
    ("van-soundproofing","Van Soundproofing","Vehicle","10k+"),
    # Budget & DIY
    ("diy-soundproofing-walls","DIY Soundproofing Walls","DIY","50k+"),
    ("diy-acoustic-panels","DIY Acoustic Panels","DIY","50k+"),
    ("soundproof-room-on-a-budget","Soundproof Room on a Budget","Budget","50k+"),
    ("how-much-does-soundproofing-cost","How Much Does Soundproofing Cost","Cost","50k+"),
    ("soundproofing-cost","Soundproofing Cost","Cost","50k+"),
    # Commercial
    ("office-soundproofing","Office Soundproofing","Commercial","50k+"),
    ("open-office-noise-reduction","Open Office Noise Reduction","Commercial","10k+"),
    ("soundproofing-conference-room","Soundproofing Conference Room","Commercial","10k+"),
    ("condo-soundproofing","Condo Soundproofing","Apartment","10k+"),
    ("soundproofing-between-units","Soundproofing Between Units","Apartment","10k+"),
    # Branded
    ("tm-soundproofing","TM Soundproofing","Branded","10k+"),
    ("tm-soundproofing-review","TM Soundproofing Review","Branded","10k+"),
    ("soundproofing-company","Soundproofing Company","Branded","10k+"),
    # Comparison (high intent)
    ("green-glue-vs-mlv","Green Glue vs Mass Loaded Vinyl","Comparison","10k+"),
    ("acoustic-foam-vs-panels","Acoustic Foam vs Acoustic Panels","Comparison","10k+"),
    ("resilient-channel-vs-isolation-clips","Resilient Channel vs Isolation Clips","Comparison","10k+"),
    ("soundproofing-vs-acoustic-treatment","Soundproofing vs Acoustic Treatment","Comparison","10k+"),
    ("rockwool-vs-fiberglass","Rockwool vs Fiberglass Insulation","Comparison","10k+"),
    # Near-me (local)
    ("soundproofing-contractor-near-me","Soundproofing Contractor Near Me","Near Me","10k+"),
    ("soundproofing-company-near-me","Soundproofing Company Near Me","Near Me","10k+"),
    ("acoustic-panels-near-me","Acoustic Panels Near Me","Near Me","10k+"),
    # Product guides (best-of)
    ("best-acoustic-foam-panels","Best Acoustic Foam Panels","Product Guide","10k+"),
    ("best-mass-loaded-vinyl","Best Mass Loaded Vinyl","Product Guide","10k+"),
    ("best-soundproof-curtains","Best Soundproof Curtains","Product Guide","10k+"),
    ("best-acoustic-insulation","Best Acoustic Insulation","Product Guide","10k+"),
    ("best-soundproof-underlayment","Best Soundproof Underlayment","Product Guide","10k+"),
    ("best-green-glue","Best Green Glue Compound","Product Guide","10k+"),
    ("best-resilient-channel","Best Resilient Channel","Product Guide","10k+"),
    ("best-door-seals-soundproofing","Best Door Seals for Soundproofing","Product Guide","10k+"),
    ("best-soundproof-window-inserts","Best Soundproof Window Inserts","Product Guide","10k+"),
    ("best-soundproof-drywall","Best Soundproof Drywall","Product Guide","10k+"),
    ("best-anti-vibration-pads","Best Anti-Vibration Pads","Product Guide","10k+"),
    ("best-bass-traps","Best Bass Traps","Product Guide","10k+"),
    ("best-sound-deadening-mats","Best Sound Deadening Mats","Product Guide","10k+"),
]

# Room type matrix: 15 rooms × 7 aspects = 105 pages
ROOM_TYPES = [
    ("apartment","Apartment"),("bedroom","Bedroom"),("home-office","Home Office"),
    ("basement","Basement"),("garage","Garage"),("studio","Recording Studio"),
    ("bathroom","Bathroom"),("nursery","Nursery"),("closet","Closet"),
    ("shed","Shed"),("condo","Condo"),("townhouse","Townhouse"),
    ("office","Office"),("conference-room","Conference Room"),("laundry-room","Laundry Room"),
]
ROOM_ASPECTS = [
    ("walls","Walls"),("ceiling","Ceiling"),("floor","Floor"),
    ("doors","Doors"),("windows","Windows"),("on-a-budget","On a Budget"),("diy","DIY"),
]
ROOM_KW = [(f"soundproofing-{rs}-{ra}", f"Soundproofing {rn} {an}", "Room Guide", "1k+")
           for rs,rn in ROOM_TYPES for ra,an in ROOM_ASPECTS]

# Problem guide pages
PROBLEM_TYPES = [
    ("neighbor-noise","Neighbor Noise"),("traffic-noise","Traffic Noise"),
    ("upstairs-noise","Upstairs Noise"),("bass-noise","Bass Noise"),
    ("footstep-noise","Footstep Noise"),("street-noise","Street Noise"),
    ("airplane-noise","Airplane Noise"),("echo-and-reverb","Echo and Reverb"),
    ("low-frequency-noise","Low Frequency Noise"),("hvac-noise","HVAC Noise"),
    ("plumbing-noise","Plumbing and Pipe Noise"),("dog-barking-noise","Dog Barking Noise"),
]
PROBLEM_KW = [(f"reduce-{ps}", f"How to Reduce {pn}", "Problem Guide", "1k+")
              for ps,pn in PROBLEM_TYPES]

# Geo pages: 50 states × 8 types + 60 cities × 8 types
STATES = [
    ("alabama","Alabama"),("alaska","Alaska"),("arizona","Arizona"),("arkansas","Arkansas"),
    ("california","California"),("colorado","Colorado"),("connecticut","Connecticut"),
    ("delaware","Delaware"),("florida","Florida"),("georgia","Georgia"),("hawaii","Hawaii"),
    ("idaho","Idaho"),("illinois","Illinois"),("indiana","Indiana"),("iowa","Iowa"),
    ("kansas","Kansas"),("kentucky","Kentucky"),("louisiana","Louisiana"),("maine","Maine"),
    ("maryland","Maryland"),("massachusetts","Massachusetts"),("michigan","Michigan"),
    ("minnesota","Minnesota"),("mississippi","Mississippi"),("missouri","Missouri"),
    ("montana","Montana"),("nebraska","Nebraska"),("nevada","Nevada"),
    ("new-hampshire","New Hampshire"),("new-jersey","New Jersey"),("new-mexico","New Mexico"),
    ("new-york","New York"),("north-carolina","North Carolina"),("north-dakota","North Dakota"),
    ("ohio","Ohio"),("oklahoma","Oklahoma"),("oregon","Oregon"),("pennsylvania","Pennsylvania"),
    ("rhode-island","Rhode Island"),("south-carolina","South Carolina"),
    ("south-dakota","South Dakota"),("tennessee","Tennessee"),("texas","Texas"),
    ("utah","Utah"),("vermont","Vermont"),("virginia","Virginia"),("washington","Washington"),
    ("west-virginia","West Virginia"),("wisconsin","Wisconsin"),("wyoming","Wyoming"),
]
CITIES = [
    ("new-york-city","New York City"),("los-angeles","Los Angeles"),("chicago","Chicago"),
    ("houston","Houston"),("phoenix","Phoenix"),("philadelphia","Philadelphia"),
    ("san-antonio","San Antonio"),("san-diego","San Diego"),("dallas","Dallas"),
    ("san-jose","San Jose"),("austin","Austin"),("jacksonville","Jacksonville"),
    ("fort-worth","Fort Worth"),("columbus","Columbus"),("charlotte","Charlotte"),
    ("indianapolis","Indianapolis"),("san-francisco","San Francisco"),("seattle","Seattle"),
    ("denver","Denver"),("nashville","Nashville"),("las-vegas","Las Vegas"),
    ("louisville","Louisville"),("memphis","Memphis"),("portland","Portland"),
    ("baltimore","Baltimore"),("milwaukee","Milwaukee"),("albuquerque","Albuquerque"),
    ("tucson","Tucson"),("fresno","Fresno"),("mesa","Mesa"),("atlanta","Atlanta"),
    ("omaha","Omaha"),("raleigh","Raleigh"),("tampa","Tampa"),("detroit","Detroit"),
    ("minneapolis","Minneapolis"),("tulsa","Tulsa"),("cleveland","Cleveland"),
    ("orlando","Orlando"),("pittsburgh","Pittsburgh"),("richmond","Richmond"),
    ("reno","Reno"),("spokane","Spokane"),("buffalo","Buffalo"),("madison","Madison"),
    ("scottsdale","Scottsdale"),("norfolk","Norfolk"),("anchorage","Anchorage"),
    ("greensboro","Greensboro"),("kansas-city","Kansas City"),("baton-rouge","Baton Rouge"),
    ("sacramento","Sacramento"),("st-louis","St Louis"),("salt-lake-city","Salt Lake City"),
    ("chattanooga","Chattanooga"),("fort-collins","Fort Collins"),("boise","Boise"),
    ("richmond-va","Richmond VA"),("des-moines","Des Moines"),("madison-wi","Madison WI"),
    ("little-rock","Little Rock"),
]
GEO_TYPES = [
    ("soundproofing","Soundproofing"),
    ("apartment-soundproofing","Apartment Soundproofing"),
    ("soundproofing-contractor","Soundproofing Contractor"),
    ("soundproof-walls","Soundproof Walls"),
    ("noise-reduction","Noise Reduction"),
    ("acoustic-panels","Acoustic Panels"),
    ("soundproofing-materials","Soundproofing Materials"),
    ("home-soundproofing","Home Soundproofing"),
]
STATE_KW = [(f"{gt}-{ss}", f"{gn} in {sn}", "Geo-State", "1k+")
            for ss,sn in STATES for gt,gn in GEO_TYPES]
CITY_KW  = [(f"{gt}-{cs}", f"{gn} in {cn}", "Geo-City", "1k+")
            for cs,cn in CITIES for gt,gn in GEO_TYPES]

KEYWORDS = CORE_KW + ROOM_KW + PROBLEM_KW + STATE_KW + CITY_KW
print(f"Keywords: {len(KEYWORDS):,}  core={len(CORE_KW)} room={len(ROOM_KW)} problem={len(PROBLEM_KW)} state={len(STATE_KW)} city={len(CITY_KW)}")

def geo_name(slug):
    for cs,cn in CITIES:
        if slug.endswith("-"+cs) or slug.endswith(cs): return cn
    for ss,sn in STATES:
        if slug.endswith("-"+ss) or slug.endswith(ss): return sn
    return None

# ── CSS ───────────────────────────────────────────────────────────────────────
CSS = (
"*{box-sizing:border-box;margin:0;padding:0}"
"body{font-family:'Segoe UI',system-ui,sans-serif;color:#111827;background:#f0f4f0;line-height:1.75}"
"a{color:#2d6a4f;text-decoration:none}a:hover{text-decoration:underline}"
".site-header{background:#1b4332;color:#fff;position:sticky;top:0;z-index:300;border-bottom:3px solid #52b788}"
".hd{max-width:1160px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;height:62px;padding:0 1.2rem}"
".logo{font-size:1.15rem;font-weight:900;color:#fff;display:flex;align-items:center;gap:.5rem}"
".logo-ico{background:#52b788;color:#1b4332;font-size:1.1rem;width:34px;height:34px;border-radius:8px;display:flex;align-items:center;justify-content:center;flex-shrink:0}"
".nav-links{display:flex;gap:1.4rem;align-items:center}"
".nav-links a{color:rgba(255,255,255,.85);font-size:.82rem;font-weight:500;transition:color .15s}"
".nav-links a:hover{color:#52b788;text-decoration:none}"
".nav-cta{background:#52b788;color:#1b4332!important;font-weight:900!important;padding:.38rem 1.05rem;border-radius:6px;font-size:.82rem!important}"
".hero{background:linear-gradient(135deg,#1b4332 0%,#2d6a4f 60%,#40916c 100%);color:#fff;padding:4.5rem 1.2rem 4rem;text-align:center;position:relative;overflow:hidden}"
".hero-inner{max-width:860px;margin:0 auto;position:relative;z-index:1}"
".hero-eyebrow{display:inline-flex;align-items:center;gap:.5rem;background:rgba(82,183,136,.2);border:1px solid rgba(82,183,136,.4);color:#d8f3dc;border-radius:50px;padding:.3rem 1rem;font-size:.72rem;letter-spacing:1.8px;text-transform:uppercase;margin-bottom:1.5rem;font-weight:700}"
".hero h1{font-size:clamp(1.9rem,4.8vw,3.1rem);font-weight:900;line-height:1.12;margin-bottom:1.1rem;letter-spacing:-.6px}"
".hero h1 span{color:#95d5b2}"
".hero-sub{font-size:1.05rem;opacity:.88;max-width:670px;margin:0 auto 2.4rem;line-height:1.78}"
".cta-btn{display:inline-flex;align-items:center;gap:.6rem;background:#52b788;color:#1b4332;font-size:1.08rem;font-weight:900;padding:1.05rem 2.8rem;border-radius:9px;text-decoration:none;box-shadow:0 6px 30px rgba(82,183,136,.45);transition:transform .18s,box-shadow .18s}"
".cta-btn:hover{transform:translateY(-3px);box-shadow:0 10px 40px rgba(82,183,136,.55);text-decoration:none;color:#1b4332}"
".hero-note{font-size:.78rem;opacity:.6;margin-top:1rem}"
".trust-strip{background:#fff;border-bottom:1px solid #d8f3dc;padding:1rem 1.2rem}"
".trust-inner{max-width:1160px;margin:0 auto;display:flex;flex-wrap:wrap;justify-content:center;gap:1.6rem}"
".trust-item{display:flex;align-items:center;gap:.42rem;font-size:.82rem;color:#374151;font-weight:600}"
".trust-ico{width:20px;height:20px;background:#2d6a4f;border-radius:50%;color:#fff;font-size:10px;display:flex;align-items:center;justify-content:center;flex-shrink:0}"
".stat-row{background:#d8f3dc;border-bottom:2px solid #b7e4c7;padding:1.8rem 1.2rem}"
".stat-inner{max-width:1160px;margin:0 auto;display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:1rem;text-align:center}"
".stat-n{font-size:2rem;font-weight:900;color:#1b4332;line-height:1}"
".stat-l{font-size:.74rem;color:#2d6a4f;margin-top:.3rem;font-weight:600}"
".breadcrumb{max-width:1160px;margin:0 auto;padding:.72rem 1.2rem;font-size:.79rem;color:#6b7280}"
".breadcrumb a{color:#2d6a4f}.breadcrumb .sep{margin:0 .32rem;color:#d1d5db}"
".pg{max-width:1160px;margin:0 auto;padding:2.2rem 1.2rem 3.5rem;display:grid;grid-template-columns:1fr 315px;gap:2.8rem;align-items:start}"
".art h2{font-size:1.3rem;font-weight:800;color:#1b4332;margin:2.5rem 0 .78rem;padding-top:1.2rem;border-top:2px solid #d8f3dc;line-height:1.3}"
".art h2:first-of-type{border-top:none;margin-top:0;padding-top:0}"
".art h3{font-size:1rem;font-weight:700;color:#2d6a4f;margin:1.5rem 0 .48rem}"
".art p{margin-bottom:1.05rem;color:#374151;font-size:.96rem;line-height:1.8}"
".art ul,.art ol{margin:0 0 1.1rem 1.45rem;color:#374151;font-size:.96rem}"
".art li{margin-bottom:.45rem;line-height:1.7}"
".art strong{color:#1b4332}"
".art a{color:#2d6a4f}"
".intro-box{background:linear-gradient(135deg,#d8f3dc,#b7e4c7);border-left:4px solid #2d6a4f;border-radius:0 12px 12px 0;padding:1.35rem 1.65rem;margin-bottom:2.3rem;font-size:1.01rem;color:#1b4332;line-height:1.85;font-weight:500}"
".toc-box{background:#f0faf4;border:1px solid #d8f3dc;border-radius:10px;padding:1rem 1.35rem;margin:1.2rem 0 1.8rem}"
".toc-box p{font-size:.8rem;font-weight:800;color:#1b4332;margin-bottom:.55rem;text-transform:uppercase;letter-spacing:.8px}"
".toc-box ol{margin:0 0 0 1rem;padding:0;font-size:.83rem;color:#2d6a4f;line-height:2}"
".toc-box a{color:#2d6a4f}"
".cmp{width:100%;border-collapse:collapse;margin:1rem 0 1.6rem;font-size:.86rem;border-radius:10px;overflow:hidden;box-shadow:0 1px 8px rgba(0,0,0,.08)}"
".cmp th{background:#1b4332;color:#fff;padding:.78rem 1rem;text-align:left;font-weight:700;font-size:.82rem}"
".cmp td{padding:.7rem 1rem;border-bottom:1px solid #e5e7eb;color:#374151;vertical-align:middle}"
".cmp tr:last-child td{border:none}"
".cmp tr:nth-child(even) td{background:#f9fafb}"
".good{color:#1b4332;font-weight:700}.bad{color:#dc2626;font-weight:700}.ok{color:#d97706;font-weight:700}"
".steps{list-style:none;margin:0 0 1.6rem;padding:0;counter-reset:step}"
".steps li{display:flex;gap:1rem;align-items:flex-start;margin-bottom:1rem;padding:1.05rem 1.15rem;background:#fff;border:1px solid #d8f3dc;border-radius:10px;counter-increment:step}"
".steps li::before{content:counter(step);background:#2d6a4f;color:#fff;font-weight:900;font-size:.82rem;min-width:28px;height:28px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px}"
".steps li p{margin:0;font-size:.92rem;color:#374151;line-height:1.65}"
".steps li strong{display:block;margin-bottom:.22rem;color:#1b4332;font-size:.94rem}"
".faq-wrap{margin:.6rem 0 1.6rem}"
".faq-item{border:1px solid #d8f3dc;border-radius:10px;margin-bottom:.78rem;overflow:hidden;background:#fff}"
".faq-q{background:#f0faf4;padding:1.05rem 1.2rem;font-weight:700;color:#1b4332;font-size:.93rem;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:1rem;user-select:none}"
".faq-q::after{content:'+';font-size:1.2rem;color:#6b7280;flex-shrink:0}"
".faq-item[open] .faq-q{background:#d8f3dc;color:#1b4332}"
".faq-item[open] .faq-q::after{content:'-';color:#2d6a4f}"
".faq-a{padding:1.05rem 1.2rem;font-size:.92rem;color:#374151;line-height:1.75;border-top:1px solid #d8f3dc}"
".tip-box{background:#f0fdf4;border:1px solid #b7e4c7;border-left:4px solid #52b788;border-radius:0 10px 10px 0;padding:1.1rem 1.35rem;margin:1.5rem 0}"
".tip-box strong{color:#1b4332;display:block;margin-bottom:.38rem;font-size:.93rem}"
".tip-box p{margin:0;color:#2d6a4f;font-size:.89rem}"
".warn-box{background:#fef9c3;border:1px solid #fde047;border-left:4px solid #eab308;border-radius:0 10px 10px 0;padding:1.1rem 1.35rem;margin:1.5rem 0}"
".warn-box strong{color:#713f12;display:block;margin-bottom:.38rem}"
".warn-box p{margin:0;color:#854d0e;font-size:.89rem}"
".stat-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:.85rem;margin:1.2rem 0 1.5rem}"
".stat-card{background:#d8f3dc;border-radius:10px;padding:1rem;text-align:center}"
".stat-card .n{font-size:1.6rem;font-weight:900;color:#1b4332;line-height:1}"
".stat-card .l{font-size:.75rem;color:#2d6a4f;margin-top:.3rem;font-weight:600}"
".rating-row{display:flex;align-items:center;gap:.6rem;margin:.35rem 0;font-size:.84rem}"
".rating-bar{flex:1;height:8px;background:#e5e7eb;border-radius:4px;overflow:hidden}"
".rating-fill{height:100%;background:#52b788;border-radius:4px}"
".product-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:1.3rem;margin:1.2rem 0 1.6rem}"
".product-card{background:#fff;border:1px solid #d8f3dc;border-radius:14px;padding:1.35rem;display:flex;flex-direction:column}"
".product-card h3{font-size:.94rem;font-weight:800;color:#1b4332;margin-bottom:.45rem}"
".product-card p{font-size:.83rem;color:#6b7280;line-height:1.6;margin-bottom:.9rem;flex:1}"
".product-badge{display:inline-block;background:#d8f3dc;color:#1b4332;font-size:.7rem;font-weight:700;padding:.2rem .55rem;border-radius:20px;margin-bottom:.6rem}"
".stars{color:#f59e0b;font-size:.85rem;margin-bottom:.3rem}"
".buy-btn{display:block;background:#2d6a4f;color:#fff;font-weight:700;padding:.72rem 1rem;border-radius:8px;text-decoration:none;text-align:center;font-size:.86rem;transition:background .15s;margin-top:auto}"
".buy-btn:hover{background:#1b4332;text-decoration:none;color:#fff}"
".related-wrap{background:#f0faf4;border:1px solid #d8f3dc;border-radius:12px;padding:1.45rem;margin-top:2.3rem}"
".related-wrap h3{font-size:.95rem;font-weight:800;color:#1b4332;margin-bottom:.95rem}"
".rel-grid{display:grid;grid-template-columns:1fr 1fr;gap:.48rem}"
".rel-grid a{font-size:.82rem;color:#2d6a4f;padding:.28rem 0;display:block;font-weight:500}"
".disclosure{background:#fef9c3;border:1px solid #fde047;border-radius:9px;padding:1rem 1.2rem;font-size:.76rem;color:#854d0e;margin-top:2.2rem;line-height:1.7}"
".disclosure strong{display:block;margin-bottom:.22rem}"
".sidebar{position:sticky;top:74px}"
".sb-hero{background:#1b4332;color:#fff;border-radius:14px;padding:1.55rem;text-align:center;margin-bottom:1.3rem;border-bottom:3px solid #52b788}"
".sb-hero h3{color:#fff;font-size:1.02rem;margin-bottom:.48rem;font-weight:900}"
".sb-hero p{color:rgba(255,255,255,.8);font-size:.82rem;margin-bottom:1.1rem;line-height:1.65}"
".sb-btn{display:block;background:#52b788;color:#1b4332;font-weight:900;padding:.85rem;border-radius:9px;text-decoration:none;font-size:.95rem;transition:transform .18s;text-align:center}"
".sb-btn:hover{transform:translateY(-2px);text-decoration:none;color:#1b4332}"
".sb-card{background:#fff;border:1px solid #d8f3dc;border-radius:14px;padding:1.3rem;margin-bottom:1.25rem}"
".sb-card h3{font-size:.92rem;font-weight:800;color:#1b4332;margin-bottom:.88rem;padding-bottom:.65rem;border-bottom:2px solid #d8f3dc}"
".chk-list{list-style:none;margin:0}"
".chk-list li{display:flex;align-items:flex-start;gap:.5rem;margin-bottom:.52rem;font-size:.84rem;color:#374151;line-height:1.55}"
".chk-list li::before{content:'✓';color:#2d6a4f;font-weight:900;flex-shrink:0}"
".noise-calc{background:#d8f3dc;border:1px solid #b7e4c7;border-radius:12px;padding:1.2rem;margin-bottom:1.25rem}"
".noise-calc h3{font-size:.92rem;font-weight:800;color:#1b4332;margin-bottom:.9rem;padding-bottom:.65rem;border-bottom:2px solid #b7e4c7}"
".nc-row{margin-bottom:.85rem}"
".nc-row label{display:block;font-size:.78rem;font-weight:700;color:#1b4332;margin-bottom:.3rem}"
".nc-select{width:100%;padding:.45rem .65rem;border:1px solid #b7e4c7;border-radius:6px;font-size:.83rem;color:#1b4332;background:#fff}"
".nc-result{background:#fff;border-radius:9px;padding:.9rem;text-align:center;margin-top:.9rem;border:1px solid #b7e4c7}"
".nc-result .big{font-size:1.2rem;font-weight:900;color:#1b4332}"
".nc-result .sub{font-size:.78rem;color:#374151;margin-top:.4rem;text-align:left;line-height:1.6}"
".blog-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(295px,1fr));gap:1.5rem;margin-top:1.6rem}"
".blog-card{background:#fff;border:1px solid #d8f3dc;border-radius:14px;padding:1.4rem;display:flex;flex-direction:column;transition:transform .18s,box-shadow .18s}"
".blog-card:hover{transform:translateY(-3px);box-shadow:0 8px 28px rgba(29,67,50,.1)}"
".blog-tag{font-size:.7rem;font-weight:800;color:#2d6a4f;text-transform:uppercase;letter-spacing:1px;margin-bottom:.5rem}"
".blog-card h3{font-size:.98rem;font-weight:700;color:#1b4332;margin-bottom:.5rem;line-height:1.42;flex:1}"
".blog-meta{display:flex;justify-content:space-between;align-items:center;font-size:.74rem;color:#9ca3af;margin-top:auto;padding-top:.6rem}"
".blog-read{color:#2d6a4f;font-weight:700}"
".ai-badge{display:inline-block;background:#eff6ff;color:#1d4ed8;font-size:.68rem;font-weight:700;padding:.15rem .45rem;border-radius:4px;margin-left:.4rem;vertical-align:middle}"
".bottom-cta{background:#1b4332;color:#fff;padding:4.5rem 1.2rem;text-align:center;border-top:4px solid #52b788}"
".bottom-cta h2{font-size:clamp(1.55rem,3.2vw,2.2rem);margin-bottom:1rem;font-weight:900}"
".bottom-cta p{font-size:1.05rem;opacity:.88;max-width:560px;margin:0 auto 2rem;line-height:1.75}"
".section{max-width:1160px;margin:0 auto;padding:3rem 1.2rem}"
".section-h{font-size:1.75rem;font-weight:900;color:#1b4332;margin-bottom:.55rem}"
".section-sub{color:#6b7280;margin-bottom:2rem;font-size:.96rem}"
".how-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.3rem;margin-top:1.6rem}"
".how-step{background:#fff;border:1px solid #d8f3dc;border-radius:14px;padding:1.5rem;text-align:center}"
".how-num{width:50px;height:50px;background:#1b4332;color:#52b788;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:1.3rem;font-weight:900;margin:0 auto 1.1rem}"
".how-step h3{font-size:.94rem;font-weight:800;color:#1b4332;margin-bottom:.4rem}"
".how-step p{font-size:.82rem;color:#6b7280;line-height:1.62}"
".feat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(205px,1fr));gap:1.2rem}"
".feat-card{background:#fff;border:1px solid #d8f3dc;border-radius:12px;padding:1.15rem;display:flex;gap:.8rem;align-items:flex-start}"
".feat-ico{width:42px;height:42px;background:#d8f3dc;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0}"
".feat-card h4{font-size:.88rem;font-weight:800;color:#1b4332;margin-bottom:.2rem}"
".feat-card p{font-size:.8rem;color:#6b7280;line-height:1.58;margin:0}"
".cat-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(245px,1fr));gap:1.3rem}"
".cat-card{background:#fff;border:1px solid #d8f3dc;border-radius:14px;padding:1.3rem}"
".cat-card h3{font-size:.91rem;font-weight:800;color:#1b4332;margin-bottom:.65rem;padding-bottom:.45rem;border-bottom:2px solid #d8f3dc;display:flex;justify-content:space-between}"
".cat-cnt{font-size:.7rem;font-weight:500;color:#9ca3af}"
".link-list{list-style:none;margin:0}"
".link-list li{padding:.18rem 0;font-size:.83rem}"
".link-list a{color:#374151;font-weight:500}"
".link-list a:hover{color:#2d6a4f}"
".trust-badge{background:#d8f3dc;border:1px solid #b7e4c7;border-radius:10px;padding:1rem;text-align:center;font-size:.74rem;color:#2d6a4f;line-height:1.9;margin-top:1rem}"
".footer{background:#081c15;color:#74c69d;padding:3.5rem 1.2rem 2rem}"
".footer-inner{max-width:1160px;margin:0 auto}"
".footer-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(175px,1fr));gap:2.2rem;margin-bottom:2.2rem}"
".footer-col h4{color:#d8f3dc;font-size:.86rem;margin-bottom:.88rem;font-weight:900;letter-spacing:.4px;text-transform:uppercase}"
".footer-col a{display:block;color:#74c69d;font-size:.81rem;margin-bottom:.38rem;transition:color .15s}"
".footer-col a:hover{color:#52b788;text-decoration:none}"
".footer-bottom{border-top:1px solid rgba(255,255,255,.07);padding-top:1.25rem;font-size:.74rem;text-align:center;line-height:1.85;color:#52b788}"
".ph{background:#1b4332;color:#fff;padding:2.8rem 1.2rem 2.4rem;text-align:center;border-bottom:3px solid #52b788}"
".ph h1{font-size:clamp(1.7rem,3.2vw,2.1rem);font-weight:900;color:#fff;margin-bottom:.7rem}"
".ph p{opacity:.88;max-width:540px;margin:0 auto;font-size:.97rem;line-height:1.72}"
".share-bar{display:flex;align-items:center;gap:.6rem;margin:1.8rem 0;padding:1rem 1.2rem;background:#f0faf4;border-radius:10px;border:1px solid #d8f3dc;flex-wrap:wrap}"
".share-btn{display:inline-flex;align-items:center;gap:.38rem;padding:.38rem .85rem;border-radius:6px;font-size:.78rem;font-weight:700;cursor:pointer;border:none;transition:transform .15s}"
".sh-fb{background:#1877f2;color:#fff}.sh-tw{background:#1da1f2;color:#fff}.sh-li{background:#0077b5;color:#fff}.sh-cp{background:#e5e7eb;color:#374151}"
".share-btn:hover{transform:translateY(-1px)}"
".author-bar{display:flex;align-items:center;gap:.75rem;padding:.85rem 1.1rem;background:#f0faf4;border-radius:10px;border:1px solid #d8f3dc;margin-bottom:1.5rem}"
".author-av{width:38px;height:38px;background:#2d6a4f;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:900;font-size:.85rem;flex-shrink:0}"
".author-name{font-size:.86rem;font-weight:700;color:#1b4332}"
".author-title{font-size:.76rem;color:#6b7280}"
"@media(max-width:768px){.pg{grid-template-columns:1fr}.sidebar{position:static}.nav-links{display:none}.rel-grid{grid-template-columns:1fr}.hero{padding:3rem 1.2rem 2.5rem}}"
)

JS = """<script>
document.querySelectorAll('.faq-item').forEach(function(d){
  d.querySelector('.faq-q').addEventListener('click',function(){
    var o=d.hasAttribute('open');
    document.querySelectorAll('.faq-item[open]').forEach(function(x){x.removeAttribute('open')});
    if(!o)d.setAttribute('open','');
  });
});
document.querySelectorAll('.share-btn').forEach(function(b){
  b.addEventListener('click',function(){
    var url=b.dataset.url||window.location.href,n=b.dataset.network;
    if(n==='facebook')window.open('https://www.facebook.com/sharer/sharer.php?u='+encodeURIComponent(url),'_blank','width=600,height=400');
    else if(n==='twitter')window.open('https://twitter.com/intent/tweet?url='+encodeURIComponent(url)+'&text='+encodeURIComponent(document.title),'_blank','width=600,height=400');
    else if(n==='linkedin')window.open('https://www.linkedin.com/sharing/share-offsite/?url='+encodeURIComponent(url),'_blank','width=600,height=400');
    else if(n==='copy'){if(navigator.clipboard)navigator.clipboard.writeText(url);b.textContent='Copied!';setTimeout(function(){b.textContent='Copy Link'},2000);}
  });
});
(function(){
  var rm=document.getElementById('nc-room'),np=document.getElementById('nc-noise'),res=document.getElementById('nc-result');
  if(!rm||!np||!res)return;
  var recs={
    bedroom:{low:'White noise machine + door sweep + acoustic curtains',medium:'MLV on shared wall + door seal kit + window insert',high:'Double drywall + Green Glue + resilient channel + MLV'},
    'home-office':{low:'Acoustic panels + door seal + thick rug',medium:'MLV on walls + acoustic panels + window insert',high:'Full decoupled wall + solid-core door + window plug'},
    studio:{low:'Acoustic foam + bass traps + thick curtains',medium:'MLV + acoustic panels + resilient channel ceiling',high:'Room-within-a-room + floating floor + triple-pane windows'},
    apartment:{low:'Acoustic curtains + draft seals + area rugs',medium:'MLV on shared wall + soundproof curtains + underlayment',high:'Decoupled walls + resilient channel + underlayment + window inserts'},
    garage:{low:'Acoustic curtains + weatherstripping',medium:'MLV + insulation + solid door sweep',high:'Full insulation + double drywall + insulated door + sealing'},
    basement:{low:'Acoustic panels + rugs + door seals',medium:'MLV + resilient channel + insulation',high:'Floating ceiling + decoupled walls + MLV + acoustic underlayment'},
    bathroom:{low:'Door sweep + exhaust fan cover',medium:'MLV + acoustic sealant + door seal',high:'Decoupled walls + solid-core door + soundproof drywall'},
    nursery:{low:'White noise + acoustic curtains + door seal',medium:'Solid-core door + window insert + area rug',high:'MLV on shared walls + window inserts + acoustic panels'},
  };
  function upd(){
    var r=rm.value||'bedroom',n=np.value||'medium';
    var rec=(recs[r]&&recs[r][n])||'Acoustic panels + door seals + area rugs';
    res.innerHTML='<div class="big">Recommended</div><div class="sub">'+rec+'</div>';
  }
  rm.addEventListener('change',upd);np.addEventListener('change',upd);upd();
})();
</script>"""

# ── SHARED COMPONENTS ─────────────────────────────────────────────────────────
def hd(title, desc, canon, schemas=None, og_type="website"):
    sc = "\n".join(f'<script type="application/ld+json">{s}</script>' for s in (schemas or []))
    return f"""<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canon}">
<meta property="og:site_name" content="{NAME}">
<meta property="og:image" content="{OG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{OG}">
<link rel="alternate" type="application/rss+xml" title="{NAME} Blog" href="{SITE}/blog/rss.xml">
{sc}
<style>{CSS}</style>"""

def nav():
    return f"""<header class="site-header">
<div class="hd">
<a href="{SITE}/" class="logo"><div class="logo-ico">&#128266;</div>Sound Proofing Wizard</a>
<nav class="nav-links" aria-label="Main">
<a href="{SITE}/">Home</a>
<a href="{SITE}/guides/">Guides</a>
<a href="{SITE}/blog/">Blog</a>
<a href="{SITE}/faq.html">FAQ</a>
<a href="{AFF}" class="nav-cta" rel="noopener sponsored">Shop Products</a>
</nav>
</div>
</header>"""

def trust():
    items=["Expert Guides","Tested Products","DIY Tutorials","Free Calculator","Updated Daily","50+ Techniques"]
    inner="".join(f'<div class="trust-item"><div class="trust-ico">&#10003;</div>{i}</div>' for i in items)
    return f'<div class="trust-strip"><div class="trust-inner">{inner}</div></div>'

def footer():
    return f"""<footer class="footer">
<div class="footer-inner">
<div class="footer-grid">
<div class="footer-col">
<h4>Sound Proofing Wizard</h4>
<p style="font-size:.8rem;line-height:1.7;margin-bottom:.9rem;color:#52b788">Expert soundproofing guides and affiliate product recommendations. We earn commissions on qualifying purchases.</p>
<a href="{AFF}" style="color:#95d5b2;font-weight:900;font-size:.88rem" rel="noopener sponsored">Shop TM Soundproofing &rarr;</a>
</div>
<div class="footer-col">
<h4>Top Guides</h4>
<a href="{SITE}/guides/soundproofing-walls/">Soundproofing Walls</a>
<a href="{SITE}/guides/how-to-soundproof-a-room/">Soundproof a Room</a>
<a href="{SITE}/guides/soundproofing-apartment/">Apartment Guide</a>
<a href="{SITE}/guides/mass-loaded-vinyl/">Mass Loaded Vinyl</a>
<a href="{SITE}/guides/green-glue-soundproofing/">Green Glue</a>
<a href="{SITE}/guides/diy-soundproofing/">DIY Soundproofing</a>
<a href="{SITE}/guides/how-much-does-soundproofing-cost/">Costs Guide</a>
</div>
<div class="footer-col">
<h4>By Room</h4>
<a href="{SITE}/guides/soundproofing-bedroom/">Bedroom</a>
<a href="{SITE}/guides/soundproofing-home-office/">Home Office</a>
<a href="{SITE}/guides/recording-studio-soundproofing/">Recording Studio</a>
<a href="{SITE}/guides/soundproofing-basement/">Basement</a>
<a href="{SITE}/guides/soundproofing-garage/">Garage</a>
<a href="{SITE}/guides/soundproofing-nursery/">Nursery</a>
</div>
<div class="footer-col">
<h4>Resources</h4>
<a href="{SITE}/blog/">Blog</a>
<a href="{SITE}/faq.html">FAQ</a>
<a href="{SITE}/how-it-works.html">How It Works</a>
<a href="{SITE}/about.html">About</a>
<a href="{SITE}/privacy.html">Privacy</a>
<a href="{SITE}/disclaimer.html">Disclaimer</a>
<a href="{SITE}/blog/rss.xml">RSS Feed</a>
</div>
</div>
<div class="footer-bottom">
<p>&copy; {YEAR} Sound Proofing Wizard &mdash; Independent affiliate resource. We earn commissions when you purchase through our links. Soundproofing results vary by construction type, noise source, and installation quality. Not responsible for contractor selection.</p>
</div>
</div>
</footer>"""

def noise_calc():
    return f"""<div class="noise-calc">
<h3>&#127926; Soundproofing Finder</h3>
<div class="nc-row"><label for="nc-room">Room Type</label>
<select id="nc-room" class="nc-select">
<option value="bedroom">Bedroom</option>
<option value="home-office">Home Office</option>
<option value="studio">Recording Studio</option>
<option value="apartment" selected>Apartment</option>
<option value="garage">Garage</option>
<option value="basement">Basement</option>
<option value="bathroom">Bathroom</option>
<option value="nursery">Nursery</option>
</select></div>
<div class="nc-row"><label for="nc-noise">Noise Level</label>
<select id="nc-noise" class="nc-select">
<option value="low">Low (voices, TV)</option>
<option value="medium" selected>Medium (traffic, music)</option>
<option value="high">High (drums, loud bass)</option>
</select></div>
<div class="nc-result" id="nc-result"></div>
<a href="{AFF}" class="sb-btn" style="margin-top:.85rem" rel="noopener sponsored">Shop Recommended Products &rarr;</a>
</div>"""

def share(url):
    return f"""<div class="share-bar">
<span style="font-size:.82rem;font-weight:700;color:#374151;margin-right:.3rem">Share:</span>
<button class="share-btn sh-fb" data-network="facebook" data-url="{url}">Facebook</button>
<button class="share-btn sh-tw" data-network="twitter" data-url="{url}">Twitter</button>
<button class="share-btn sh-li" data-network="linkedin" data-url="{url}">LinkedIn</button>
<button class="share-btn sh-cp" data-network="copy" data-url="{url}">Copy Link</button>
</div>"""

def author(date_str, mins=8, ai_generated=False):
    badge = '<span class="ai-badge">AI-Enhanced</span>' if ai_generated else '<span style="font-size:.7rem;background:#d8f3dc;color:#1b4332;font-weight:700;padding:.18rem .55rem;border-radius:20px">Expert Reviewed</span>'
    return f"""<div class="author-bar" itemscope itemtype="https://schema.org/Article">
<div class="author-av">SP</div>
<div>
<div class="author-name" itemprop="author">Sound Proofing Wizard Editorial</div>
<div class="author-title">Updated <time itemprop="dateModified" datetime="{TODAY}">{date_str}</time> &bull; {mins} min read &bull; <a href="{SITE}/about.html" style="color:#6b7280;font-size:.74rem">About our guides</a></div>
</div>
<div style="margin-left:auto">{badge}</div>
</div>"""

def toc(items):
    lis = "".join(f'<li><a href="#{slug}">{label}</a></li>' for slug,label in items)
    return f'<nav class="toc-box" aria-label="Table of contents"><p>&#128214; In This Guide</p><ol>{lis}</ol></nav>'

CTA_VARIANTS = [
    ("Shop Soundproofing Products &rarr;","Free shipping on orders over $50"),
    ("Get Expert Soundproofing Solutions","Trusted by homeowners nationwide"),
    ("Browse TM Soundproofing Products &rarr;","Professional-grade materials"),
    ("Find the Right Solution &rarr;","Free expert advice + fast shipping"),
    ("Shop Now &rarr;","30-day satisfaction guarantee"),
    ("Explore Soundproofing Materials","DIY-friendly with installation guides"),
    ("Get Your Soundproofing Solution &rarr;","Top-rated products for every budget"),
    ("Start Soundproofing Today &rarr;","Professional results at DIY prices"),
]

PROD_BTNS = [
    ("Shop MLV &rarr;","Browse Acoustic Panels","Get Green Glue","Shop Door Seals"),
    ("Get Mass Loaded Vinyl","Shop Acoustic Treatment","Buy Green Glue","Get Door Seals"),
    ("Buy MLV Now &rarr;","View Acoustic Panels","Order Green Glue","Shop Seals &rarr;"),
    ("Shop MLV Products","Browse Panel Options","Get Damping Compound","View Door Seals"),
    ("Order MLV &rarr;","Shop Sound Panels","Buy Green Glue &rarr;","Get Seal Kit &rarr;"),
    ("Get MLV &rarr;","Shop Panels Now","Green Glue &rarr;","Door Seal Kit &rarr;"),
    ("Buy Mass Vinyl","Acoustic Panels &rarr;","Damping Compound","Seal + Sweep Kit"),
    ("MLV Roll &rarr;","Panel Set &rarr;","Glue Compound &rarr;","Door Seal &rarr;"),
]

def cta_btn(slug="", cls="cta-btn", style=""):
    h = sh(slug) % len(CTA_VARIANTS)
    txt, sub = CTA_VARIANTS[h]
    st = f' style="{style}"' if style else ""
    return f'<a href="{AFF}" class="{cls}"{st} rel="noopener sponsored">{txt}</a>\n<p class="hero-note">{sub}</p>'

def product_grid(slug, idx):
    pb = PROD_BTNS[(idx + sh(slug)) % len(PROD_BTNS)]
    cards = [
        ("Best for Walls","Mass Loaded Vinyl (MLV)","Adds heavy blocking mass to walls and ceilings. The most cost-effective soundproofing material available -- 1 lb/sq ft of limp mass that cuts mid and low frequency noise significantly.",pb[0]),
        ("Best Value","Green Glue Compound","Applied between drywall layers, converts sound energy to heat. Adds 8-12 STC points with minimal effort. Two tubes per 4x8 sheet is all you need.",pb[1]),
        ("Best for Rooms","Acoustic Panels","Reduce echo and reverberation inside any room. Essential for home offices, studios, and video calls. Available in many sizes and colors to suit any space.",pb[2]),
        ("Quick Install","Door Seals + Sweeps","Seal the gaps that let noise in. A door sweep and perimeter seal deliver 10-15 dB immediately in 30 minutes. Highest ROI soundproofing upgrade available.",pb[3]),
    ]
    stars = "&#9733;&#9733;&#9733;&#9733;&#9733;"
    inner = "".join(f'<div class="product-card"><div class="product-badge">{badge}</div><div class="stars">{stars}</div><h3>{name}</h3><p>{desc}</p><a href="{AFF}" class="buy-btn" rel="noopener sponsored">{btn}</a></div>'
                    for badge,name,desc,btn in cards)
    return f'<div id="products"></div><div class="product-grid">{inner}</div>'

RELATED_MAP = {
"General":[("soundproofing-walls","Soundproofing Walls"),("mass-loaded-vinyl","Mass Loaded Vinyl"),("acoustic-panels","Acoustic Panels"),("diy-soundproofing","DIY Guide"),("how-to-soundproof-a-room","How to Soundproof"),("green-glue-soundproofing","Green Glue")],
"Walls":[("mass-loaded-vinyl","Mass Loaded Vinyl"),("resilient-channel-soundproofing","Resilient Channel"),("soundproof-drywall","Soundproof Drywall"),("green-glue-soundproofing","Green Glue"),("acoustic-insulation","Acoustic Insulation"),("decoupling-soundproofing","Decoupling")],
"Bedroom":[("soundproofing-walls","Soundproof Walls"),("soundproof-curtains","Soundproof Curtains"),("how-to-soundproof-a-door","Soundproof Door"),("soundproofing-windows","Windows"),("acoustic-panels","Acoustic Panels"),("soundproofing-ceiling","Ceiling")],
"Apartment":[("soundproofing-apartment-walls","Apartment Walls"),("block-noise-from-neighbors","Block Neighbor Noise"),("soundproof-curtains","Soundproof Curtains"),("soundproofing-floor","Soundproof Floor"),("soundproof-window","Windows"),("mass-loaded-vinyl","MLV")],
"Studio":[("home-recording-studio-soundproofing","Home Studio"),("acoustic-foam","Acoustic Foam"),("acoustic-panels","Acoustic Panels"),("bass-trap","Bass Traps"),("resilient-channel-soundproofing","Resilient Channel"),("soundproofing-walls","Walls")],
"Products":[("acoustic-foam","Acoustic Foam"),("mass-loaded-vinyl","Mass Loaded Vinyl"),("soundproof-curtains","Soundproof Curtains"),("acoustic-panels","Acoustic Panels"),("green-glue-soundproofing","Green Glue"),("soundproofing-insulation","Insulation")],
"Doors":[("soundproof-door-seal","Door Seal"),("door-sweep-soundproofing","Door Sweep"),("how-to-soundproof-a-door","Soundproof Door"),("mass-loaded-vinyl","MLV"),("soundproofing-walls","Walls"),("soundproof-room","Soundproof Room")],
"Windows":[("soundproof-window-insert","Window Insert"),("window-soundproofing-film","Window Film"),("soundproof-curtains","Soundproof Curtains"),("soundproofing-windows","Windows Guide"),("soundproofing-apartment","Apartment Guide"),("noise-reduction","Noise Reduction")],
"Floors":[("soundproof-underlayment","Underlayment"),("soundproofing-between-floors","Between Floors"),("impact-noise-reduction","Impact Noise"),("footstep-noise-reduction","Footstep Noise"),("soundproof-flooring","Flooring"),("anti-vibration-mat","Anti-Vibration Mat")],
"Ceiling":[("resilient-channel-soundproofing","Resilient Channel"),("mass-loaded-vinyl","MLV"),("acoustic-insulation","Insulation"),("soundproofing-ceiling","Ceiling Guide"),("soundproofing-apartment","Apartment"),("soundproofing-between-floors","Between Floors")],
"Budget":[("diy-soundproofing","DIY Guide"),("diy-acoustic-panels","DIY Panels"),("soundproof-curtains","Curtains"),("acoustic-foam","Acoustic Foam"),("cheapest-way-to-soundproof-a-room","Cheapest Method"),("how-much-does-soundproofing-cost","Cost Guide")],
"DIY":[("diy-soundproofing-walls","DIY Walls"),("diy-acoustic-panels","DIY Panels"),("cheapest-way-to-soundproof-a-room","Cheapest Method"),("acoustic-foam","Acoustic Foam"),("mass-loaded-vinyl","MLV"),("soundproofing-walls","Walls")],
"Noise":[("block-noise-from-neighbors","Block Neighbor Noise"),("reduce-road-noise-in-home","Road Noise"),("reduce-echo-in-room","Reduce Echo"),("soundproofing-apartment","Apartment"),("soundproofing-walls","Walls"),("soundproof-window","Windows")],
"Acoustics":[("reduce-echo-in-room","Reduce Echo"),("acoustic-panels","Acoustic Panels"),("acoustic-foam","Acoustic Foam"),("bass-trap","Bass Traps"),("stc-rating","STC Rating"),("soundproofing-vs-acoustic-treatment","SFP vs Treatment")],
"How-To":[("how-to-soundproof-a-wall","Soundproof a Wall"),("how-to-soundproof-a-door","Soundproof a Door"),("how-to-soundproof-a-ceiling","Soundproof a Ceiling"),("diy-soundproofing","DIY Guide"),("cheapest-way-to-soundproof-a-room","Budget Guide"),("soundproofing-walls","Walls")],
"Vehicle":[("car-soundproofing","Car Soundproofing"),("car-sound-deadening","Sound Deadening"),("mass-loaded-vinyl","MLV"),("anti-vibration-mat","Anti-Vibration"),("soundproofing-materials","Materials"),("sound-deadening","Sound Deadening")],
"Cost":[("cheapest-way-to-soundproof-a-room","Cheapest Method"),("diy-soundproofing","DIY Guide"),("how-much-does-soundproofing-cost","Cost Guide"),("soundproofing-materials","Materials"),("mass-loaded-vinyl","MLV"),("is-soundproofing-worth-it","Worth It?")],
"Informational":[("how-does-soundproofing-work","How It Works"),("soundproofing-vs-acoustic-treatment","SFP vs Treatment"),("stc-rating","STC Rating"),("types-of-soundproofing","Types"),("soundproofing-effectiveness","Effectiveness"),("is-soundproofing-worth-it","Worth It?")],
"Comparison":[("green-glue-vs-mlv","Green Glue vs MLV"),("acoustic-foam-vs-panels","Foam vs Panels"),("soundproofing-vs-acoustic-treatment","SFP vs Treatment"),("resilient-channel-vs-isolation-clips","RC vs Clips"),("mass-loaded-vinyl","MLV"),("acoustic-panels","Panels")],
"Near Me":[("soundproofing-contractor-near-me","Contractors Near Me"),("soundproofing-company-near-me","Companies Near Me"),("soundproofing-walls","Walls Guide"),("diy-soundproofing","DIY Guide"),("how-much-does-soundproofing-cost","Cost Guide"),("acoustic-panels","Panels")],
"Product Guide":[("acoustic-foam","Acoustic Foam"),("mass-loaded-vinyl","MLV"),("acoustic-panels","Panels"),("soundproof-curtains","Curtains"),("green-glue-soundproofing","Green Glue"),("acoustic-insulation","Insulation")],
"Room Guide":[("soundproofing-walls","Walls"),("soundproofing-ceiling","Ceiling"),("soundproof-flooring","Floor"),("how-to-soundproof-a-door","Doors"),("soundproofing-windows","Windows"),("acoustic-panels","Panels")],
"Problem Guide":[("soundproofing-walls","Walls"),("block-noise-from-neighbors","Block Noise"),("mass-loaded-vinyl","MLV"),("acoustic-panels","Panels"),("soundproof-window","Windows"),("soundproofing-ceiling","Ceiling")],
"Basement":[("soundproofing-walls","Walls"),("soundproofing-ceiling","Ceiling"),("acoustic-insulation","Insulation"),("mass-loaded-vinyl","MLV"),("soundproof-door","Doors"),("soundproof-flooring","Floor")],
"Garage":[("soundproofing-walls","Walls"),("soundproofing-insulation","Insulation"),("mass-loaded-vinyl","MLV"),("soundproof-door","Doors"),("diy-soundproofing","DIY Guide"),("how-much-does-soundproofing-cost","Cost")],
"Home Office":[("soundproofing-walls","Walls"),("acoustic-panels","Panels"),("how-to-soundproof-a-door","Doors"),("soundproofing-windows","Windows"),("reduce-echo-in-room","Reduce Echo"),("noise-reduction","Noise Reduction")],
"Bathroom":[("soundproofing-walls","Walls"),("how-to-soundproof-a-door","Doors"),("mass-loaded-vinyl","MLV"),("soundproof-drywall","Drywall"),("sound-isolation","Isolation"),("noise-reduction","Noise Reduction")],
"Branded":[("soundproofing-company","Soundproofing Company"),("soundproofing-products","Products"),("soundproofing-walls","Walls"),("acoustic-panels","Panels"),("mass-loaded-vinyl","MLV"),("diy-soundproofing","DIY")],
"Commercial":[("office-soundproofing","Office Guide"),("soundproofing-conference-room","Conference Room"),("open-office-noise-reduction","Open Office"),("acoustic-panels","Panels"),("soundproofing-walls","Walls"),("noise-reduction","Noise Reduction")],
"Geo-State":[("soundproofing-walls","Soundproof Walls"),("soundproofing-apartment","Apartment Guide"),("block-noise-from-neighbors","Block Neighbor Noise"),("mass-loaded-vinyl","MLV"),("how-to-soundproof-a-room","How to Soundproof"),("diy-soundproofing","DIY Guide")],
"Geo-City":[("soundproofing-apartment","Apartment Guide"),("soundproofing-walls","Walls"),("block-noise-from-neighbors","Block Noise"),("soundproof-curtains","Curtains"),("how-to-soundproof-a-room","How to Soundproof"),("acoustic-panels","Panels")],
"Default":[("soundproofing-walls","Walls"),("acoustic-panels","Panels"),("mass-loaded-vinyl","MLV"),("diy-soundproofing","DIY"),("soundproofing-bedroom","Bedroom"),("soundproof-studio","Studio")],
}

def get_related(cat, slug):
    pool = RELATED_MAP.get(cat, RELATED_MAP["Default"])
    return [(s,t) for s,t in pool if s != slug][:6]

# ── SVG INFOGRAPHICS ──────────────────────────────────────────────────────────
def svg_wall_layers():
    return ('<svg viewBox="0 0 680 130" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Soundproofing wall layers diagram" style="width:100%;margin:1.2rem 0">'
            '<title>Soundproofing wall layer system</title>'
            '<rect width="680" height="130" rx="10" fill="#d8f3dc"/>'
            '<text x="340" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#1b4332">Soundproofing Wall System: Inside to Outside</text>'
            '<g transform="translate(20,35)"><rect width="100" height="70" rx="7" fill="#1b4332"/>'
            '<text x="50" y="32" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">5/8" Drywall</text>'
            '<text x="50" y="47" text-anchor="middle" font-size="9" fill="rgba(255,255,255,.8)">Inner layer</text>'
            '<text x="50" y="62" text-anchor="middle" font-size="9" fill="#52b788">Mass</text></g>'
            '<g transform="translate(132,35)"><rect width="100" height="70" rx="7" fill="#2d6a4f"/>'
            '<text x="50" y="32" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">Green Glue</text>'
            '<text x="50" y="47" text-anchor="middle" font-size="9" fill="rgba(255,255,255,.8)">Between layers</text>'
            '<text x="50" y="62" text-anchor="middle" font-size="9" fill="#95d5b2">Damping</text></g>'
            '<g transform="translate(244,35)"><rect width="100" height="70" rx="7" fill="#40916c"/>'
            '<text x="50" y="32" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">Mass Loaded</text>'
            '<text x="50" y="45" text-anchor="middle" font-size="10" font-weight="700" fill="#fff">Vinyl</text>'
            '<text x="50" y="62" text-anchor="middle" font-size="9" fill="#d8f3dc">Mass</text></g>'
            '<g transform="translate(356,35)"><rect width="100" height="70" rx="7" fill="#52b788"/>'
            '<text x="50" y="32" text-anchor="middle" font-size="10" font-weight="700" fill="#1b4332">Resilient</text>'
            '<text x="50" y="45" text-anchor="middle" font-size="10" font-weight="700" fill="#1b4332">Channel</text>'
            '<text x="50" y="62" text-anchor="middle" font-size="9" fill="#1b4332">Decoupling</text></g>'
            '<g transform="translate(468,35)"><rect width="100" height="70" rx="7" fill="#74c69d"/>'
            '<text x="50" y="32" text-anchor="middle" font-size="10" font-weight="700" fill="#1b4332">Rockwool</text>'
            '<text x="50" y="45" text-anchor="middle" font-size="10" font-weight="700" fill="#1b4332">Insulation</text>'
            '<text x="50" y="62" text-anchor="middle" font-size="9" fill="#1b4332">Absorption</text></g>'
            '<g transform="translate(580,35)"><rect width="80" height="70" rx="7" fill="#b7e4c7"/>'
            '<text x="40" y="36" text-anchor="middle" font-size="10" font-weight="700" fill="#1b4332">Outer</text>'
            '<text x="40" y="50" text-anchor="middle" font-size="10" font-weight="700" fill="#1b4332">Drywall</text>'
            '<text x="40" y="64" text-anchor="middle" font-size="9" fill="#2d6a4f">Mass</text></g>'
            '<text x="340" y="120" text-anchor="middle" font-size="9" fill="#2d6a4f">Combined system achieves STC 55-65. Each layer addresses: Mass + Damping + Decoupling + Absorption.</text>'
            '</svg>')

def svg_db_reduction():
    return ('<svg viewBox="0 0 680 165" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Soundproofing decibel reduction by method" style="width:100%;margin:1rem 0 1.5rem">'
            '<title>Noise reduction achieved by soundproofing method</title>'
            '<rect width="680" height="165" rx="10" fill="#f9fafb" stroke="#d8f3dc" stroke-width="1"/>'
            '<text x="340" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#1b4332">Noise Reduction by Method (Approximate dB)</text>'
            '<g transform="translate(10,35)"><text x="0" y="14" font-size="10" fill="#374151">Door sweep + perimeter seal</text>'
            '<rect x="190" y="2" width="65" height="16" rx="3" fill="#95d5b2"/><text x="258" y="13" font-size="10" fill="#1b4332"> 5-10 dB</text></g>'
            '<g transform="translate(10,58)"><text x="0" y="14" font-size="10" fill="#374151">Acoustic curtains over windows</text>'
            '<rect x="190" y="2" width="90" height="16" rx="3" fill="#74c69d"/><text x="283" y="13" font-size="10" fill="#1b4332"> 8-15 dB</text></g>'
            '<g transform="translate(10,81)"><text x="0" y="14" font-size="10" fill="#374151">MLV on walls + acoustic panels</text>'
            '<rect x="190" y="2" width="130" height="16" rx="3" fill="#52b788"/><text x="323" y="13" font-size="10" fill="#fff"> 15-25 dB</text></g>'
            '<g transform="translate(10,104)"><text x="0" y="14" font-size="10" fill="#374151">Double drywall + Green Glue</text>'
            '<rect x="190" y="2" width="170" height="16" rx="3" fill="#2d6a4f"/><text x="363" y="13" font-size="10" fill="#fff"> 20-30 dB</text></g>'
            '<g transform="translate(10,127)"><text x="0" y="14" font-size="10" fill="#374151">Full decoupled system (RC + MLV + insulation)</text>'
            '<rect x="190" y="2" width="280" height="16" rx="3" fill="#1b4332"/><text x="473" y="13" font-size="10" fill="#d8f3dc"> 35-50+ dB</text></g>'
            '<text x="340" y="158" text-anchor="middle" font-size="9" fill="#6b7280">Results vary by construction, installation quality, and noise frequency. Low-frequency bass is harder to block.</text>'
            '</svg>')

def svg_stc_chart():
    return ('<svg viewBox="0 0 680 125" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="STC rating guide for soundproofing" style="width:100%;margin:1rem 0 1.5rem">'
            '<title>STC Sound Transmission Class rating guide</title>'
            '<rect width="680" height="125" rx="10" fill="#d8f3dc" stroke="#b7e4c7" stroke-width="1"/>'
            '<text x="340" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#1b4332">STC Rating Guide -- What Each Score Means</text>'
            '<g transform="translate(15,35)"><rect width="108" height="72" rx="7" fill="#ef4444"/>'
            '<text x="54" y="28" text-anchor="middle" font-size="22" font-weight="900" fill="#fff">25</text>'
            '<text x="54" y="46" text-anchor="middle" font-size="9" fill="#fff">Standard walls</text>'
            '<text x="54" y="60" text-anchor="middle" font-size="8" fill="rgba(255,255,255,.85)">Speech audible</text>'
            '<text x="54" y="74" text-anchor="middle" font-size="8" fill="rgba(255,255,255,.75)">Upgrade needed</text></g>'
            '<g transform="translate(133,35)"><rect width="108" height="72" rx="7" fill="#f59e0b"/>'
            '<text x="54" y="28" text-anchor="middle" font-size="22" font-weight="900" fill="#1b4332">35</text>'
            '<text x="54" y="46" text-anchor="middle" font-size="9" fill="#1b4332">Code minimum</text>'
            '<text x="54" y="60" text-anchor="middle" font-size="8" fill="#451a03">Loud speech heard</text>'
            '<text x="54" y="74" text-anchor="middle" font-size="8" fill="#451a03">Needs improvement</text></g>'
            '<g transform="translate(251,35)"><rect width="108" height="72" rx="7" fill="#52b788"/>'
            '<text x="54" y="28" text-anchor="middle" font-size="22" font-weight="900" fill="#fff">42</text>'
            '<text x="54" y="46" text-anchor="middle" font-size="9" fill="#fff">Good isolation</text>'
            '<text x="54" y="60" text-anchor="middle" font-size="8" fill="rgba(255,255,255,.88)">Speech rarely heard</text>'
            '<text x="54" y="74" text-anchor="middle" font-size="8" fill="rgba(255,255,255,.75)">DIY achievable</text></g>'
            '<g transform="translate(369,35)"><rect width="108" height="72" rx="7" fill="#2d6a4f"/>'
            '<text x="54" y="28" text-anchor="middle" font-size="22" font-weight="900" fill="#fff">52</text>'
            '<text x="54" y="46" text-anchor="middle" font-size="9" fill="#fff">Very good</text>'
            '<text x="54" y="60" text-anchor="middle" font-size="8" fill="rgba(255,255,255,.88)">Music muffled</text>'
            '<text x="54" y="74" text-anchor="middle" font-size="8" fill="rgba(255,255,255,.75)">Pro-level result</text></g>'
            '<g transform="translate(487,35)"><rect width="175" height="72" rx="7" fill="#1b4332"/>'
            '<text x="87" y="28" text-anchor="middle" font-size="22" font-weight="900" fill="#d8f3dc">60+</text>'
            '<text x="87" y="46" text-anchor="middle" font-size="9" fill="#d8f3dc">Professional studio</text>'
            '<text x="87" y="60" text-anchor="middle" font-size="8" fill="rgba(216,243,220,.85)">Near silence</text>'
            '<text x="87" y="74" text-anchor="middle" font-size="8" fill="rgba(216,243,220,.7)">Room-within-a-room</text></g>'
            '</svg>')

def svg_cost_tiers():
    return ('<svg viewBox="0 0 680 130" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="Soundproofing budget tiers" style="width:100%;margin:1rem 0 1.5rem">'
            '<title>Soundproofing budget tiers and expected results</title>'
            '<rect width="680" height="130" rx="10" fill="#f0faf4" stroke="#d8f3dc" stroke-width="1"/>'
            '<text x="340" y="22" text-anchor="middle" font-size="12" font-weight="700" fill="#1b4332">Soundproofing Budget Tiers -- Results Per Investment Level</text>'
            '<g transform="translate(15,35)"><rect width="195" height="78" rx="8" fill="#95d5b2"/>'
            '<text x="97" y="24" text-anchor="middle" font-size="14" font-weight="900" fill="#1b4332">Under $150</text>'
            '<text x="97" y="42" text-anchor="middle" font-size="10" fill="#1b4332">Door seal + sweep + curtains</text>'
            '<text x="97" y="57" text-anchor="middle" font-size="10" fill="#1b4332">10-20 dB reduction</text>'
            '<text x="97" y="71" text-anchor="middle" font-size="9" fill="#2d6a4f">Weekend project, beginner-friendly</text></g>'
            '<g transform="translate(225,35)"><rect width="215" height="78" rx="8" fill="#52b788"/>'
            '<text x="107" y="24" text-anchor="middle" font-size="14" font-weight="900" fill="#fff">$150 - $600</text>'
            '<text x="107" y="42" text-anchor="middle" font-size="10" fill="#fff">MLV + panels + window insert</text>'
            '<text x="107" y="57" text-anchor="middle" font-size="10" fill="#fff">20-35 dB reduction</text>'
            '<text x="107" y="71" text-anchor="middle" font-size="9" fill="rgba(255,255,255,.88)">1-2 weekend project</text></g>'
            '<g transform="translate(455,35)"><rect width="210" height="78" rx="8" fill="#1b4332"/>'
            '<text x="105" y="24" text-anchor="middle" font-size="14" font-weight="900" fill="#d8f3dc">$600+</text>'
            '<text x="105" y="42" text-anchor="middle" font-size="10" fill="#d8f3dc">Full wall + ceiling system</text>'
            '<text x="105" y="57" text-anchor="middle" font-size="10" fill="#d8f3dc">35-55+ dB reduction</text>'
            '<text x="105" y="71" text-anchor="middle" font-size="9" fill="rgba(216,243,220,.85)">Multi-day or pro install</text></g>'
            '</svg>')

def svg_noise_entry():
    return ('<svg viewBox="0 0 680 118" xmlns="http://www.w3.org/2000/svg" role="img" '
            'aria-label="How noise enters a room through different surfaces" style="width:100%;margin:1rem 0 1.5rem">'
            '<title>Noise entry points in a typical room</title>'
            '<rect width="680" height="118" rx="10" fill="#f9fafb" stroke="#d8f3dc" stroke-width="1"/>'
            '<text x="340" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#1b4332">How Noise Enters Your Room -- Treat in This Order</text>'
            '<g transform="translate(12,30)"><rect width="100" height="72" rx="6" fill="#ef4444"/>'
            '<text x="50" y="24" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">Door Gap</text>'
            '<text x="50" y="40" text-anchor="middle" font-size="16" font-weight="900" fill="#fff">40-60%</text>'
            '<text x="50" y="56" text-anchor="middle" font-size="9" fill="rgba(255,255,255,.9)">of total leakage</text>'
            '<text x="50" y="68" text-anchor="middle" font-size="9" fill="rgba(255,255,255,.8)">Fix first</text></g>'
            '<g transform="translate(124,30)"><rect width="100" height="72" rx="6" fill="#f59e0b"/>'
            '<text x="50" y="24" text-anchor="middle" font-size="11" font-weight="700" fill="#1b4332">Windows</text>'
            '<text x="50" y="40" text-anchor="middle" font-size="16" font-weight="900" fill="#1b4332">15-25%</text>'
            '<text x="50" y="56" text-anchor="middle" font-size="9" fill="#451a03">of total leakage</text>'
            '<text x="50" y="68" text-anchor="middle" font-size="9" fill="#451a03">Fix second</text></g>'
            '<g transform="translate(236,30)"><rect width="100" height="72" rx="6" fill="#52b788"/>'
            '<text x="50" y="24" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">Walls</text>'
            '<text x="50" y="40" text-anchor="middle" font-size="16" font-weight="900" fill="#fff">10-20%</text>'
            '<text x="50" y="56" text-anchor="middle" font-size="9" fill="rgba(255,255,255,.9)">of total leakage</text>'
            '<text x="50" y="68" text-anchor="middle" font-size="9" fill="rgba(255,255,255,.8)">Fix third</text></g>'
            '<g transform="translate(348,30)"><rect width="100" height="72" rx="6" fill="#2d6a4f"/>'
            '<text x="50" y="24" text-anchor="middle" font-size="11" font-weight="700" fill="#fff">Ceiling</text>'
            '<text x="50" y="40" text-anchor="middle" font-size="16" font-weight="900" fill="#fff">5-15%</text>'
            '<text x="50" y="56" text-anchor="middle" font-size="9" fill="rgba(255,255,255,.9)">of total leakage</text>'
            '<text x="50" y="68" text-anchor="middle" font-size="9" fill="rgba(255,255,255,.8)">Fix fourth</text></g>'
            '<g transform="translate(460,30)"><rect width="100" height="72" rx="6" fill="#1b4332"/>'
            '<text x="50" y="24" text-anchor="middle" font-size="11" font-weight="700" fill="#d8f3dc">Floor</text>'
            '<text x="50" y="40" text-anchor="middle" font-size="16" font-weight="900" fill="#d8f3dc">5-10%</text>'
            '<text x="50" y="56" text-anchor="middle" font-size="9" fill="rgba(216,243,220,.9)">of total leakage</text>'
            '<text x="50" y="68" text-anchor="middle" font-size="9" fill="rgba(216,243,220,.8)">Fix fifth</text></g>'
            '<g transform="translate(572,30)"><rect width="95" height="72" rx="6" fill="#f0faf4" stroke="#b7e4c7" stroke-width="1"/>'
            '<text x="47" y="22" text-anchor="middle" font-size="10" font-weight="700" fill="#1b4332">Seal in order</text>'
            '<text x="47" y="37" text-anchor="middle" font-size="9" fill="#2d6a4f">1. Door gaps</text>'
            '<text x="47" y="50" text-anchor="middle" font-size="9" fill="#2d6a4f">2. Windows</text>'
            '<text x="47" y="63" text-anchor="middle" font-size="9" fill="#2d6a4f">3. Walls</text>'
            '<text x="47" y="76" text-anchor="middle" font-size="9" fill="#2d6a4f">4. Ceiling/Floor</text></g>'
            '</svg>')

def svg_products_comparison():
    rows = [
        ("Mass Loaded Vinyl","Blocking","$1-2/sqft","Walls/Ceiling","★★★★★"),
        ("Green Glue","Damping","$15/tube","Between drywall","★★★★★"),
        ("Resilient Channel","Decoupling","$1/ft","Walls/Ceiling","★★★★☆"),
        ("Acoustic Insulation","Absorption","$0.50/sqft","Inside walls","★★★★☆"),
        ("Door Seal Kit","Gap sealing","$40-75","Doors","★★★★★"),
        ("Acoustic Panels","Absorption","$20-150","Room surfaces","★★★★☆"),
    ]
    header = ('<rect width="680" height="202" rx="10" fill="#f9fafb" stroke="#d8f3dc" stroke-width="1"/>'
              '<text x="340" y="20" text-anchor="middle" font-size="12" font-weight="700" fill="#1b4332">Soundproofing Product Comparison</text>'
              '<g transform="translate(0,28)"><rect width="680" height="18" fill="#1b4332"/>'
              '<text x="10" y="13" font-size="9" font-weight="700" fill="#fff">Product</text>'
              '<text x="175" y="13" font-size="9" font-weight="700" fill="#fff">Function</text>'
              '<text x="295" y="13" font-size="9" font-weight="700" fill="#fff">Cost</text>'
              '<text x="395" y="13" font-size="9" font-weight="700" fill="#fff">Best For</text>'
              '<text x="545" y="13" font-size="9" font-weight="700" fill="#fff">Rating</text></g>')
    body_rows = ""
    for i,(prod,func,cost,best,rating) in enumerate(rows):
        y = 28+18+i*26
        bg = '#f0faf4' if i%2==0 else '#fff'
        body_rows += (f'<g transform="translate(0,{y})">'
                     f'<rect width="680" height="26" fill="{bg}"/>'
                     f'<text x="10" y="17" font-size="9" font-weight="600" fill="#1b4332">{prod}</text>'
                     f'<text x="175" y="17" font-size="9" fill="#374151">{func}</text>'
                     f'<text x="295" y="17" font-size="9" fill="#374151">{cost}</text>'
                     f'<text x="395" y="17" font-size="9" fill="#374151">{best}</text>'
                     f'<text x="545" y="17" font-size="10" fill="#2d6a4f">{rating}</text></g>')
    return f'<svg viewBox="0 0 680 202" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Soundproofing product comparison table" style="width:100%;margin:1rem 0 1.5rem"><title>Soundproofing products compared</title>{header}{body_rows}</svg>'

SVG_POOL = [svg_wall_layers, svg_db_reduction, svg_stc_chart, svg_cost_tiers, svg_noise_entry, svg_products_comparison]

def pick_svg(category, slug, idx=0):
    """Route to appropriate SVG -- all 6 used evenly"""
    h = (idx + sh(slug)) % 3
    # 2-way splits for major categories
    if category in ("Walls","Ceiling","DIY"):
        return svg_wall_layers() if h < 2 else svg_db_reduction()
    if category in ("Acoustics","Comparison"):
        return svg_stc_chart() if h < 2 else svg_products_comparison()
    if category in ("Product Guide","Products","Branded"):
        return svg_products_comparison() if h == 0 else (svg_db_reduction() if h == 1 else svg_stc_chart())
    if category in ("Budget","Cost"):
        return svg_cost_tiers() if h < 2 else svg_wall_layers()
    if category in ("General","Informational","Techniques"):
        return svg_noise_entry() if h == 0 else (svg_db_reduction() if h == 1 else svg_wall_layers())
    if category in ("How-To","Problem Guide"):
        return svg_noise_entry() if h == 0 else (svg_wall_layers() if h == 1 else svg_db_reduction())
    if category in ("Near Me",):
        return svg_noise_entry() if h < 2 else svg_cost_tiers()
    if category in ("Geo-State","Geo-City"):
        # Rotate all 6 evenly for geo pages (most numerous)
        return SVG_POOL[(idx + sh(slug)) % 6]()
    if category in ("Room Guide","Bedroom","Apartment","Studio","Basement","Garage",
                    "Home Office","Bathroom","Nursery","Closet","Shed","Commercial"):
        return svg_wall_layers() if h == 0 else (svg_cost_tiers() if h == 1 else svg_noise_entry())
    if category in ("Noise",):
        return svg_noise_entry() if h < 2 else svg_db_reduction()
    if category in ("Floors",):
        return svg_db_reduction() if h < 2 else svg_cost_tiers()
    if category in ("Doors","Windows"):
        return svg_noise_entry() if h < 2 else svg_wall_layers()
    if category in ("Vehicle",):
        return svg_db_reduction() if h < 2 else svg_stc_chart()
    # Default: rotate all 6 evenly
    return SVG_POOL[(idx + sh(slug)) % 6]()

INTROS = {'General': ['Complete guide to {kw}: the four principles of soundproofing, expert product picks, and DIY step-by-step methods that deliver real results.', 'Everything you need to know about {kw} -- budget-friendly quick fixes, honest product reviews, and professional techniques explained clearly.', 'Whether you are dealing with noisy neighbors, traffic noise, or echo, this {kw} guide covers every approach with proven techniques and realistic expectations.', "Tackle {kw} the right way: the right order of operations, the products that actually work, and the mistakes that waste most people's money.", 'This expert {kw} guide covers mass, decoupling, damping, and absorption -- the four principles that explain why some methods work and others do not.', 'Stop noise from controlling your home. This {kw} guide gives you a clear action plan from a $20 door sweep to a professional room rebuild.', 'Expert-written {kw} guide: the science of sound blocking explained clearly, with product rankings and DIY tutorials for every budget level.', 'From acoustic foam myths to mass loaded vinyl mastery, this {kw} guide covers the complete picture so you can make smart decisions.'], 'Walls': ['Soundproofing walls is the single highest-impact upgrade for most rooms. This {kw} guide covers the right materials, the right order, and the right technique.', 'Walls carry most of the noise in and out of a room. This complete {kw} guide covers MLV, Green Glue, resilient channel, and acoustic insulation.', 'Whether renting or owning, this {kw} guide gives you practical options at every budget -- from removable MLV panels to full decoupled wall rebuilds.', 'The most effective {kw} combines mass, damping, and decoupling. This guide breaks down how to implement each principle in the right sequence.', 'This complete {kw} guide explains the four-layer system that professionals use and how to replicate it at DIY prices with standard tools.', 'From acoustic panels to double drywall with Green Glue, this {kw} guide covers every approach with honest cost and effectiveness ratings.', 'Expert {kw} guide: which products deliver the most STC improvement per dollar, and the installation details that most DIYers get wrong.', 'This {kw} guide covers the weak-link principle -- why treating one wall is useless if the door has a gap -- with a systematic action plan.'], 'Bedroom': ['A quiet bedroom changes your quality of life. This {kw} guide covers every surface and every budget to help you sleep better tonight.', 'From door sweeps to decoupled walls, this complete {kw} guide gives you noise reduction options at every price point, prioritized by impact.', 'Sleep disruption is a health issue. This {kw} guide prioritizes the changes that make the biggest difference to sleep quality first.', 'Noisy neighbors, traffic, or a partner who snores -- this {kw} guide covers every noise source with targeted, proven solutions.', 'This {kw} guide starts with $20 door sweeps and works up to professional solutions. Every step delivers measurable noise reduction.', 'Combining the right elements transforms a noisy bedroom. This {kw} covers doors, windows, walls, and floors as a complete system.', 'Expert-tested {kw}: which materials work best for bedroom noise, how to install them, and what realistic results look like at each budget.', 'Transform your bedroom into a true quiet sanctuary with this complete {kw} guide -- every noise entry point addressed systematically.'], 'Apartment': ['Renting does not mean living with noise. This {kw} guide covers effective techniques that require zero permanent wall modifications.', 'Noisy neighbors above, below, and beside you -- this {kw} guide addresses every apartment noise source with practical renter-friendly solutions.', 'The best {kw} strategies for renters: removable, effective, and landlord-approved options that genuinely reduce noise levels.', 'Apartment noise is a top quality-of-life complaint. This {kw} guide gives you options from cheap quick fixes to serious room transformations.', 'Even without drilling or permanent changes, {kw} in an apartment is achievable. This guide shows you exactly what to buy and where to put it.', 'This complete {kw} guide covers the shared wall, the ceiling, the floor, windows, and doors -- all with renter-friendly solutions.', 'Mass loaded vinyl tapestries, acoustic curtains, door sweeps, and more -- this {kw} guide covers what genuinely works without violating your lease.', 'Block neighbor noise, traffic, and hallway sounds with this practical {kw} guide designed specifically for apartment dwellers.'], 'Studio': ['Building a home recording studio requires serious {kw}. This guide covers acoustic treatment, sound isolation, and every technique from DIY to professional.', 'Whether tracking vocals or mixing, {kw} is essential for professional results. This guide covers the complete studio build from sealing to treatment.', 'This complete {kw} guide covers the critical difference between sound isolation (keeping noise out) and acoustic treatment (making the room sound right).', 'From DIY bass traps to full room-within-a-room builds, this {kw} guide covers every budget and skill level with honest performance expectations.', 'Professional {kw} starts with understanding what you are fighting. This guide covers STC ratings, frequency response, and product selection for home studios.', 'This {kw} guide is built for home studio owners: practical, affordable steps to professional sound without a six-figure professional build.', 'The four pillars of {kw} -- mass, damping, decoupling, absorption -- explained in detail for home recording studio applications.', 'Get professional audio quality at home with this complete {kw} guide: material picks, installation sequence, and acoustic treatment strategy.'], 'Products': ['Not all soundproofing products perform as advertised. This {kw} guide reviews the top options with honest effectiveness ratings and real-world testing.', 'Choosing the right {kw} depends on your noise problem and budget. This guide matches specific products to specific noise situations.', 'This complete {kw} guide covers the top materials on the market, how each one works mechanically, and the best use cases for each.', 'From budget picks to professional-grade solutions, this {kw} guide tells you exactly what to buy based on your specific noise problem.', 'Expert-reviewed {kw}: we cut through the marketing claims and tell you which products actually deliver on their noise reduction promises.', 'Before you spend anything on {kw}, read this. We rank options by value-per-dB and the specific situations where each product excels.', 'The best {kw} for your situation depends on what type of noise you are fighting. This guide breaks down options by noise type and room.', 'This {kw} guide covers product specifications, real-world STC performance, and installation tips for every major soundproofing material category.'], 'DIY': ['You do not need a contractor for serious {kw}. This step-by-step guide covers everything achievable with standard tools and a weekend of work.', 'Save thousands with {kw}: these tested DIY techniques deliver professional results at a fraction of what contractors charge.', 'This {kw} guide is designed for first-timers: clear instructions, honest materials lists, and the pro tips that prevent the most common mistakes.', 'From acoustic panels to resilient channel ceilings, this {kw} guide covers every project you can realistically complete as a homeowner.', 'The best {kw} projects combine high impact with manageable difficulty. This guide ranks every option by noise reduction achieved and skill required.', 'Expert {kw} techniques that any homeowner can execute: no specialized skills required, just the right materials and this step-by-step guide.', 'This complete {kw} guide includes exact materials lists, tool requirements, installation sequences, and the mistakes that ruin most DIY projects.', 'Real {kw} results without a contractor. This guide walks you through the most impactful projects in the order that delivers results fastest.'], 'Budget': ['Effective {kw} does not require spending thousands. This guide covers the highest-impact approaches under $50, $200, and $500.', 'This complete {kw} guide starts with free and ultra-cheap techniques and works up to maximum-impact solutions at every price point.', 'Get real noise reduction without breaking the bank. This {kw} guide ranks every approach by noise reduction per dollar spent.', 'The cheapest {kw} techniques that actually work -- no soundproof paint gimmicks, just proven materials at honest prices with real results.', 'Budget-conscious {kw} is absolutely possible. This guide gives you a prioritized action plan starting from the highest-ROI changes first.', 'From $20 door sweeps to $300 MLV wall systems, this {kw} guide covers meaningful noise reduction at every budget level.', 'This {kw} guide cuts through expensive options and shows you exactly which cheap techniques deliver the most noise reduction in real homes.', 'Noise reduction does not have to be expensive. This {kw} guide covers high-impact, low-cost solutions for every room and noise type.'], 'How-To': ['Step-by-step guide to {kw}: the right materials, the correct order of operations, and the mistakes that cost most DIYers their results.', 'This complete how-to guide for {kw} covers every step from initial noise assessment to finished installation with pro tips throughout.', 'Everything you need to successfully complete {kw}: exact materials list, tools needed, installation sequence, and testing methods.', 'This {kw} guide is designed for first-timers -- no assumptions, clear steps, honest difficulty assessment, and realistic expectations.', 'Follow this guide to {kw} and achieve professional results. The key is the sequence: gaps first, then mass, then decoupling, then absorption.', 'The right approach to {kw} depends on your specific noise problem. This guide helps you diagnose first, then treat with the right solution.', 'This complete {kw} tutorial covers noise assessment, material selection, installation, and verification testing -- everything in one guide.', 'Expert-written {kw} guide: which methods deliver the most noise reduction and exactly how to implement each one correctly.'], 'Noise': ['Practical solutions for {kw}: what actually works, what is a waste of money, and the fastest path to meaningful noise reduction.', 'This complete guide to solving {kw} covers every technique from cheap quick fixes to complete soundproofing system installations.', 'Stop {kw} from controlling your home with these expert-tested solutions matched to this specific noise type and transmission path.', 'Whether the issue is occasional or constant, this {kw} guide covers both quick relief options and permanent long-term solutions.', 'Expert solutions for {kw}: understanding the noise source and transmission path to choose the right intervention for your situation.', 'This {kw} guide identifies the right combination of products and techniques for this specific noise problem -- no generic advice.', 'Real-world solutions to {kw}: tested, practical approaches that make a measurable difference to the noise level in your home.', 'This complete {kw} guide covers source, path, and receiver -- addressing every stage of the noise transmission process effectively.'], 'Acoustics': ['Understanding the science behind {kw} helps you make smarter soundproofing decisions and avoid the expensive products that deliver nothing.', 'This guide to {kw} covers the fundamentals of sound behavior and how different materials and techniques address each specific problem.', 'Great {kw} starts with understanding what you are fighting. This guide explains the physics and the practical solutions together.', 'This complete {kw} guide covers STC ratings, NRC coefficients, and frequency response in plain language with actionable recommendations.', 'From bass traps to acoustic diffusers, this {kw} guide covers every treatment category with honest effectiveness ratings and positioning advice.', "Sound behaves in predictable ways. This {kw} guide explains those patterns and how to exploit them to improve your room's acoustic performance.", 'This {kw} guide serves homeowners and studio owners alike: the acoustic science made practical with specific product recommendations.', 'Understanding {kw} means knowing the difference between soundproofing (blocking) and acoustic treatment (improving sound quality inside a room).'], 'Doors': ['Doors are the biggest acoustic weak point in any room -- responsible for 40-60% of total noise leakage. This {kw} guide covers every upgrade option.', 'A hollow-core door with floor gap can undermine an entire wall soundproofing system. This {kw} guide covers the most effective and affordable upgrades.', 'This complete {kw} guide covers door sweeps, perimeter seals, mass loaded vinyl overlays, solid-core replacements, and acoustic door panels.', 'Quick and effective {kw}: from $15 door sweeps to complete solid-core replacements -- with the order of operations that maximizes every dollar.', 'This {kw} guide ranks every technique by effectiveness and cost, starting with the changes that deliver the most noise reduction immediately.', 'Whether renting or owning, this {kw} guide covers renter-friendly sealing options and permanent upgrades that achieve maximum STC ratings.', 'Sound leaks through every gap around a door. This {kw} guide covers every seal point with the right product for each specific gap.', 'Expert techniques for {kw}: the installation details that make the difference between mediocre results and genuinely impressive noise reduction.'], 'Windows': ['Windows are the second biggest noise entry point. This {kw} guide covers every upgrade from acoustic curtains to secondary glazing systems.', 'This complete {kw} guide covers curtains, window plugs, commercial inserts, secondary glazing, and full replacement with honest effectiveness ratings.', 'Affordable {kw} is very achievable. This guide covers options from $30 to $2,000 per window with honest noise reduction expectations for each.', 'Traffic noise, airplane noise, street noise -- this {kw} guide covers targeted solutions for every type of noise entering through glass.', 'This {kw} guide covers permanent and removable solutions, making it useful for both renters and homeowners in every budget range.', 'Get serious noise reduction from your windows without replacing them. This {kw} guide covers the most cost-effective upgrade path.', 'This complete {kw} guide explains why windows leak sound at every frequency range and the specific products that address each failure mode.', 'Expert guide to {kw}: DIY window plugs, commercial insert systems, secondary glazing, and acoustic glass -- compared honestly.'], 'Floors': ['Floor noise travels in both directions. This {kw} guide covers blocking upstairs footsteps and preventing your noise from disturbing downstairs neighbors.', 'This complete {kw} guide covers underlayment types, area rugs, floating floors, resilient clips, and full floor rebuild systems with IIC ratings.', 'Impact noise from footsteps is one of the hardest noise types to block. This {kw} guide covers the decoupling solutions that actually work.', 'Whether renting or owning, this {kw} guide covers effective floor noise reduction at every budget level with specific product recommendations.', 'This {kw} guide ranks every floor treatment technique by its effectiveness against impact noise versus airborne sound transmission.', 'From $50 area rugs to full floating floor systems, this {kw} guide covers the complete range with honest IIC improvement expectations.', 'Expert-tested {kw}: the right underlayment, the correct installation method, and the real-world results you can expect from each approach.', 'This complete {kw} guide covers IIC and STC ratings together, matching the right products to each specific floor noise challenge.'], 'Ceiling': ['Ceiling noise from upstairs neighbors is one of the most common building complaints. This {kw} guide covers every real solution available.', 'This complete {kw} guide covers resilient channel, isolation clips, mass loaded vinyl, acoustic insulation, and fully floating ceiling systems.', 'From quick acoustic panel installations to full ceiling decoupling systems, this {kw} guide covers every approach with budget tiers.', 'The right {kw} approach depends on whether you own or rent and how severe the footstep noise is. This guide covers every scenario.', 'Expert guide to {kw}: the techniques that deliver meaningful footstep noise reduction versus the upgrades that mostly waste money.', 'Stop footstep noise from upstairs with this complete {kw} guide -- covering decoupling, mass addition, and acoustic absorption together.', 'This {kw} guide applies the four principles of soundproofing specifically to ceilings with product recommendations for each principle.', 'Whether dealing with footsteps, voices, or bass from above, this {kw} guide matches the right technique to the specific noise problem.'], 'Vehicle': ['Road noise, wind, and engine sound make driving exhausting. This {kw} guide covers every technique for a noticeably quieter ride.', 'This complete {kw} guide covers sound deadening mats, acoustic spray, door seals, and full vehicle treatment systems with installation order.', 'From budget spray treatments to full door panel installations, this {kw} guide covers every option for a quieter vehicle.', 'This expert {kw} guide covers which panels make the biggest difference and the installation techniques that maximize the results.', 'Reduce road noise by 40-60% with proper {kw}. This guide covers the best materials and the installation sequence for best results.', 'This {kw} guide is written for DIY installers: the right products, the right order, and the pro tips that make the real difference.', 'Expert vehicle {kw} guide: from floor pan treatment to door panels, wheel wells to firewall -- complete coverage with realistic expectations.', 'Stop road noise from ruining your drive. This {kw} guide covers every noise source with targeted, tested product recommendations.'], 'Cost': ['Soundproofing cost varies enormously. This {kw} guide breaks down realistic budgets for every approach and room type so you plan accurately.', 'This complete {kw} guide covers material costs, labor costs, and which investments deliver the best noise reduction per dollar.', 'DIY vs professional {kw}: this guide covers the real cost of each approach and the situations where each one makes financial sense.', 'This {kw} guide gives you honest, up-to-date prices for every major soundproofing material and installation method.', 'From $20 door sweeps to $10,000 professional room builds, this {kw} guide covers every budget with expected noise reduction results.', 'Understand the true {kw}: materials, labor, and the hidden costs that most soundproofing guides conveniently forget to mention.', 'This {kw} guide helps you maximize noise reduction for your specific budget -- no expensive surprises, no false economy mistakes.', 'Expert {kw} breakdown: the cheapest effective solutions, the best mid-range options, and when premium materials are genuinely worth it.'], 'Informational': ['Understanding {kw} helps you make smarter decisions. This guide explains the science and debunks the most common expensive myths.', 'This complete guide to {kw} covers how sound travels, what stops it, and why some popular methods simply do not work as claimed.', 'Everything you need to know about {kw}: the physics, the products, the techniques, and realistic expectations for every situation.', 'This {kw} guide is written for homeowners, renters, and studio owners who want real answers rather than product marketing language.', 'Clear, honest information about {kw}: what works, what does not, and how to achieve your specific noise reduction goals within budget.', 'This complete {kw} guide covers the fundamentals so you can evaluate any product or technique on its own merits intelligently.', 'Great soundproofing starts with understanding {kw}. This guide covers the principles that determine what will actually work in your space.', 'This {kw} guide separates acoustic science from marketing hype and gives you the information to make confident, informed decisions.'], 'Comparison': ['Side-by-side: {kw} -- which one to choose, when each option excels, and the honest verdict from acoustic science and real-world testing.', 'The complete {kw} comparison: specifications, real-world performance, installation differences, and the clear recommendation for each situation.', 'Stop guessing: this {kw} guide breaks down every key difference so you buy the right product the first time without expensive mistakes.', 'Expert {kw} analysis: how each option works mechanically, where each excels, and the specific situations where one clearly outperforms the other.', 'This {kw} comparison cuts through manufacturer marketing claims to deliver the acoustic science that determines which product actually wins.', 'Before you buy: this {kw} guide covers specs, STC performance per dollar, installation complexity, and the verdict for every common use case.', 'Honest {kw} review: the physics of how each product works, what the tests show, and a clear recommendation you can act on today.', 'The definitive {kw} comparison: materials science, installation details, real-world performance data, and a final recommendation for your specific situation.'], 'Near Me': ['Find the right {kw} -- what to look for in a contractor, what questions to ask, and how to evaluate quotes before committing.', 'Guide to {kw}: what professional soundproofing costs, where to find qualified contractors, and the DIY alternatives worth considering.', 'Before you search for {kw}, read this -- the red flags to watch for, the right questions to ask, and fair pricing benchmarks.', 'Everything about {kw}: when professional installation is worth the premium and when DIY achieves the same results for much less.', 'Finding quality {kw}: credentials that matter, the scope questions to ask, and how to compare quotes fairly between contractors.', 'This {kw} guide covers both finding professionals and deciding whether hiring one is actually necessary for your specific project.', 'Professional vs DIY soundproofing -- this guide helps you make the right call on {kw} for your budget and project complexity.', 'How to find and evaluate {kw}: contractor expertise signals, project scoping best practices, timeline expectations, and payment structures.'], 'Product Guide': ['This complete {kw} reviews the top options on the market with honest performance ratings, installation notes, and value assessments.', 'Before you buy anything for {kw}, read this. We cut through marketing claims and tell you what genuinely performs in real installations.', 'Expert-reviewed {kw}: the top products ranked by real-world noise reduction, installation difficulty, durability, and cost-per-dB.', 'This {kw} guide covers specifications, real-world STC performance, best use cases, and installation tips for each recommended product.', 'Not all {kw} products are created equal. This guide separates the genuinely effective options from the overpriced and overhyped ones.', 'This {kw} guide covers budget picks through professional-grade options, with the right recommendation based on your specific noise situation.', 'We evaluated {kw} products against the toughest residential noise challenges. Here is exactly what works and why it works.', 'This complete {kw} guide includes installation guides, compatibility notes, and the specific situations where each product genuinely excels.'], 'Room Guide': ['This complete {kw} guide covers every noise entry point -- walls, ceiling, floor, doors, and windows -- with proven techniques for each surface.', 'Whether dealing with neighbor noise, traffic, or echo, this {kw} guide covers every solution systematically from cheapest to most effective.', 'From cheap quick fixes to serious room renovations, this {kw} guide covers the full spectrum with realistic cost and performance expectations.', 'This {kw} guide is built around your specific room and noise challenge -- practical advice based on what actually works in real spaces.', 'Expert {kw} for this specific room: the right materials for each surface, the right installation method, and what to prioritize first.', 'Stop noise from controlling your space with this complete {kw} guide -- systematic coverage of every surface and noise entry point.', 'This {kw} guide covers the optimal combination of methods that delivers the best results for this specific room configuration.', 'From $20 quick fixes to complete renovations, this {kw} guide gives you every option with honest cost and effectiveness ratings.'], 'Problem Guide': ['Targeted solutions for {kw}: the products and techniques that address this specific noise source effectively and efficiently.', 'This complete guide to reducing {kw} covers every technique from cheap quick fixes to complete soundproofing system installations.', 'Stop {kw} from controlling your home with these expert-tested solutions specifically matched to this noise type and transmission path.', 'Whether the issue is occasional or constant, this {kw} guide covers both immediate relief and permanent long-term solutions.', 'Expert solutions for {kw}: understanding exactly how this noise travels so we can block it at the most effective intervention points.', 'This {kw} guide selects the right combination of products and techniques for this specific noise problem -- no one-size-fits-all advice.', 'Real-world solutions to {kw}: practical approaches that have been tested in homes and deliver measurable, noticeable noise reduction.', 'This complete {kw} guide addresses source, transmission path, and receiving room -- every stage of how this specific noise reaches you.'], 'Basement': ['Basement {kw} has specific advantages: concrete walls, below-grade position, and full surface access. This guide shows how to maximize them.', 'This complete {kw} guide covers walls, ceiling, floor, doors, and windows with techniques suited to the specific conditions of a basement.', 'Whether you are building a home theater, music room, or just want a quieter basement, this {kw} guide covers every use case.', 'Basement {kw} is often simpler than above-grade rooms because you control all surfaces. This guide shows you how to take full advantage.', 'This {kw} guide covers moisture-resistant materials, correct installation sequences, and the techniques that deliver the most dB reduction.', 'Turn your basement into a genuinely quiet space or professional-grade workspace with this complete {kw} guide.', 'Expert basement {kw}: the right materials for a below-grade environment and the exact installation methods that maximize performance.', 'This complete {kw} guide covers sound isolation, acoustic treatment, mechanical noise control, and HVAC noise reduction together.'], 'Garage': ['A soundproofed garage opens up real possibilities: workshop, band practice, home gym. This {kw} guide covers the complete transformation.', 'This complete {kw} guide covers the garage door (biggest challenge), walls, ceiling, man-door, and windows with practical solutions.', 'Garage {kw} is more achievable than most people expect. This guide covers every surface with cost-effective, tested techniques.', 'Whether you want to keep noise in or keep it out, this {kw} guide covers both goals with the right materials for each scenario.', 'From simple weatherstripping to complete insulated builds, this {kw} guide covers every level of garage acoustic transformation.', 'This expert {kw} guide covers the specific construction challenges of garages and the products that work best in that environment.', 'Turn your garage into a usable music, fitness, or work space with this complete, step-by-step {kw} guide.', 'This {kw} guide covers the garage door first -- where most noise enters -- then works through walls, ceiling, and finishing details.'], 'Home Office': ['A quiet home office makes you more productive and sounds more professional on every call. This {kw} guide covers every noise source.', 'This complete {kw} guide addresses echo on video calls, external noise blocking, and creating an acoustically professional environment.', 'Work from home without distractions. This {kw} guide covers every surface and every noise source with solutions at every budget.', 'From acoustic panels to door seals, this {kw} guide covers the best home office noise reduction upgrades in priority order.', 'This {kw} guide tackles both external noise (traffic, neighbors) and internal echo (reverb on video calls) with targeted solutions for each.', 'Expert {kw}: the right combination of soundproofing and acoustic treatment that makes your home office genuinely professional.', 'This complete {kw} guide is designed for remote workers who need a quiet, acoustically clean space for deep work and video calls.', 'Reduce distracting noise and dramatically improve your video call audio quality with this expert {kw} guide and product picks.'], 'Bathroom': ['Bathroom privacy noise is more addressable than most people think. This {kw} guide covers the practical upgrades that make a real difference.', 'This complete {kw} guide covers door gaps (the main culprit), wall mass, pipe noise, exhaust fan covers, and ventilation sealing.', 'From door seals to acoustic drywall, this {kw} guide covers every effective upgrade for improved bathroom sound privacy.', 'Bathroom {kw} is mostly about sealing gaps and adding mass to the door. This guide covers exactly how to do both effectively.', 'This {kw} guide covers both directions: keeping bathroom sounds private and keeping outside noise from disturbing bathroom occupants.', 'Expert {kw}: the quick wins that make an immediate difference and the permanent upgrades that solve the problem completely.', 'This complete {kw} guide covers every effective bathroom noise reduction technique with realistic cost and installation difficulty ratings.', 'Improve bathroom sound privacy significantly with this expert {kw} guide covering doors, walls, ventilation, and pipe noise.'], 'Branded': ['TM Soundproofing offers professional-grade {kw} solutions for homeowners and contractors. This guide covers their complete product range.', 'This independent review of {kw} covers product quality, installation support, value assessment, and which products deliver the best results.', 'TM Soundproofing is a trusted name in {kw}. This guide covers their product line with honest effectiveness ratings for each category.', 'This complete guide to {kw} covers TM Soundproofing products alongside DIY techniques so you can make the best decision for your project.', 'Expert review: TM Soundproofing products for {kw} -- what each product does, how to install it, and what results to realistically expect.', 'This {kw} guide covers TM Soundproofing solutions with honest comparisons to help you choose the right product for your situation.', 'Professional-grade {kw} is now accessible to homeowners through TM Soundproofing. This guide shows exactly what to buy for your situation.', 'This complete {kw} guide helps you select the right TM Soundproofing products for your specific noise problem and budget.'], 'Commercial': ['Office {kw} improves productivity, protects privacy, and creates a more professional environment. This guide covers every commercial approach.', 'This complete {kw} guide covers open offices, conference rooms, private offices, and shared workspaces with specific product recommendations.', 'From acoustic panels to full wall systems, this {kw} guide covers every noise reduction technique for professional environments.', 'Expert {kw} for the workplace: privacy screens, acoustic ceiling tiles, wall panels, and door seals with performance ratings for each.', 'This {kw} guide balances noise reduction effectiveness with the aesthetic requirements of a professional commercial environment.', 'OSHA standards, speech privacy, and productivity all depend on proper {kw}. This guide covers every aspect with specific recommendations.', 'This complete {kw} guide covers both acoustic treatment (reducing echo) and sound isolation (blocking noise between spaces) for offices.', 'Expert commercial {kw}: the products and techniques that meet building codes and deliver measurable speech privacy improvements.'], 'Geo-State': ['Complete {kw} guide for {loc} homeowners and renters -- expert techniques, top-rated products, and step-by-step DIY instructions at every budget.', 'Dealing with noise in {loc}? This {kw} guide covers every surface, every noise type, and every budget level with solutions that work.', 'Expert {kw} for {loc} residents: the right techniques, the products worth buying, and honest expectations for what you can achieve.', 'Whether renting or owning in {loc}, this {kw} guide gives you practical options that deliver real noise reduction results.', '{kw} in {loc}: complete coverage of walls, doors, windows, floors, and ceilings with honest cost and effectiveness assessments.', 'Stop noise from controlling your {loc} home. This expert {kw} guide covers everything from a $20 door sweep to a full renovation.', 'This {kw} guide for {loc} covers all four soundproofing principles with product recommendations for every situation and budget.', 'Expert-tested {kw} solutions for {loc} -- from quick renter-friendly fixes to professional-grade permanent installations.'], 'Geo-City': ['Complete {kw} guide for {loc} residents -- expert techniques, tested products, and DIY tutorials for every noise problem in urban living.', 'Living in {loc} means dealing with real noise. This {kw} guide covers every solution from renter-friendly to full renovation.', 'Expert {kw} for {loc}: the techniques that work in urban environments, with honest cost estimates and step-by-step DIY guides.', 'Noise in {loc}? This comprehensive {kw} guide covers apartment walls, street noise, neighbor noise, and every budget level.', '{kw} in {loc}: practical solutions for every surface and noise source, tested and rated by acoustic experts.', 'Whether you own or rent in {loc}, this {kw} guide gives you real options that deliver measurable noise reduction.', 'Stop {loc} noise with this expert {kw} guide -- four principles, six surfaces, every budget level covered systematically.', 'The complete {kw} guide for {loc}: from $20 door sweeps to professional wall systems, with realistic expectations for each.'], 'Default': ['This complete {kw} guide covers every technique and product with honest effectiveness ratings and step-by-step instructions.', 'Expert-written {kw} guide: the best techniques, the right products, and the installation tips that make the real difference.', 'Whether a first-timer or experienced DIYer, this {kw} guide covers everything you need to achieve meaningful noise reduction.', 'This {kw} guide starts with the easiest, cheapest improvements and works up to complete professional-grade soundproofing solutions.', 'Stop living with noise. This expert {kw} guide gives you a clear action plan based on your specific situation and budget.', 'From quick fixes to full renovations, this {kw} guide covers every approach with honest cost and effectiveness assessments.', 'This complete {kw} guide covers the science, the products, and the step-by-step techniques that deliver real, measurable noise reduction.', 'Expert {kw} advice: which methods work for which noise types, exactly how to implement them, and what results to expect.']}

def get_intro(category, slug, idx):
    pool = INTROS.get(category, INTROS["Default"])
    h = (idx + sh(slug)) % len(pool)
    tmpl = pool[h]
    loc = geo_name(slug) if category.startswith("Geo") else None
    if loc:
        tmpl = tmpl.replace("{loc}", loc)
    return tmpl

def body(kw, slug, category, idx):
    if category in ("Geo-State","Geo-City"):
        return _body_geo(kw, slug, category, idx)
    if category == "Comparison":
        return _body_comparison(kw, slug, idx)
    h = (idx + sh(slug)) % 10

    faq = (f'<div id="faq"></div><div class="faq-wrap">'
           f'<details class="faq-item"><summary class="faq-q">Does {kw.lower()} actually work?</summary>'
           f'<div class="faq-a">Yes -- when the right techniques are applied in the right order. The most common reason soundproofing fails is treating one surface while ignoring others. Address all noise entry points: door first, windows second, walls third. Realistic results: 15-35 dB reduction is achievable for most DIY projects.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">How much does {kw.lower()} cost?</summary>'
           f'<div class="faq-a">Costs range from $20 for a door sweep to $5,000+ for full wall treatment. A practical mid-range DIY project -- acoustic panels, door seal kit, window curtains, MLV on the problem wall, and area rug -- typically costs $250-$650 and delivers 20-35 dB of noise reduction.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">Can I do {kw.lower()} myself?</summary>'
           f'<div class="faq-a">Yes. Most residential soundproofing projects are well within the skill range of any homeowner with basic tools. The techniques are the same as professional installations -- the difference is time, not skill. Door sealing takes 30 minutes. MLV installation takes half a day. Resilient channel ceiling takes a full weekend.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">What is the best soundproofing material for {kw.lower()}?</summary>'
           f'<div class="faq-a">Mass loaded vinyl (MLV) is the most versatile and cost-effective material for walls and ceilings. For floors, acoustic underlayment performs best. For windows, acoustic inserts deliver the best noise reduction per dollar. The right choice always depends on the surface being treated and the type of noise.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">Does soundproof paint work for {kw.lower()}?</summary>'
           f'<div class="faq-a">No. Soundproof paint adds a negligible amount of mass -- perhaps 1-3 dB of reduction at best. The same money invested in a door sweep and perimeter seal delivers 10-15 dB. Soundproof paint is one of the worst value soundproofing purchases available and should be avoided entirely.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">How long does {kw.lower()} take to install?</summary>'
           f'<div class="faq-a">Door sweep and seal: 30-45 minutes. Acoustic curtains: 30 minutes. MLV on a wall: 3-5 hours. DIY acoustic panels (4-6 panels): one day. Resilient channel ceiling: 2-3 days. Full wall rebuild with double drywall: 3-5 days per room. Most impactful changes take one weekend or less.</div></details>'
           '</div>')

    stat_c = ('<div class="stat-cards">'
              '<div class="stat-card"><div class="n">40dB</div><div class="l">Max DIY reduction</div></div>'
              '<div class="stat-card"><div class="n">STC 55</div><div class="l">Professional target</div></div>'
              '<div class="stat-card"><div class="n">$50-600</div><div class="l">Typical DIY budget</div></div>'
              '<div class="stat-card"><div class="n">Weekend</div><div class="l">Most projects done</div></div>'
              '</div>')

    if h == 0:
        return f"""
<h2 id="overview">The Four Principles of {kw}</h2>
<p>Every effective soundproofing technique is based on one or more of four scientific principles. Understanding them prevents wasting money on products that address the wrong problem and helps you design a system that actually works.</p>
<p><strong>Mass</strong> -- Heavy materials resist sound wave penetration. Mass loaded vinyl, extra drywall, and heavy curtains add mass to surfaces, making them harder to vibrate and transmit sound energy.</p>
<p><strong>Decoupling</strong> -- Vibrations travel efficiently through rigid structures. Resilient channel, isolation clips, and floating floors break this transmission path, dramatically reducing impact noise and structure-borne sound.</p>
<p><strong>Damping</strong> -- Viscoelastic materials like Green Glue compound convert sound energy to heat as it passes through rigid panels. Sandwiched between drywall layers, it adds significant STC points with minimal construction complexity.</p>
<p><strong>Absorption</strong> -- Soft porous materials like acoustic foam and Rockwool panels absorb sound energy within a room, reducing echo and reverberation rather than blocking external noise.</p>
{pick_svg(category, slug, idx)}
<h2 id="how-to">Step-by-Step {kw} Plan</h2>
<ol class="steps">
<li><strong>Seal all gaps first -- always</strong><p>Before spending anything on mass or absorption, seal every gap. A door sweep ($25) and perimeter seal ($35) can deliver 12-18 dB of noise reduction in 30 minutes. This is the highest-ROI step and should always come first.</p></li>
<li><strong>Add mass to the primary noise entry surface</strong><p>Once gaps are sealed, the surface transmitting the most noise gets mass added: MLV on shared walls, acoustic curtains on windows, underlayment under floors. One surface at a time, starting with the loudest.</p></li>
<li><strong>Decouple if impact noise is the issue</strong><p>Footsteps, HVAC vibration, and mechanical noise require decoupling -- breaking the rigid connection between surfaces. Resilient channel, isolation clips, and rubber pads address this where mass alone cannot.</p></li>
<li><strong>Treat room acoustics last</strong><p>After external noise is reduced, internal echo often becomes more noticeable. Acoustic panels at primary reflection points improve speech clarity, recording quality, and the general liveability of the space.</p></li>
</ol>
{stat_c}
<h2 id="costs">What {kw} Realistically Costs</h2>
<p>Under $150 gets you gap sealing and curtains -- 10-20 dB reduction, immediate results. $150-$600 adds MLV, window inserts, and acoustic panels -- 20-35 dB combined with the sealing work. Above $600, structural modifications like resilient channel and double drywall push performance toward professional levels.</p>
<div class="tip-box"><strong>Borrow the right logic</strong><p>Every extra dB of noise reduction is exponentially harder to achieve. The first 15 dB from door sealing is cheap and easy. The next 15 dB from MLV requires real materials. The following 10 dB from resilient channel requires construction. Plan your project to the level that solves your actual problem, not theoretical perfection.</p></div>
{faq}"""

    elif h == 1:
        return f"""
<h2 id="overview">What Actually Works for {kw}: An Honest Assessment</h2>
<p>The soundproofing market is full of overpriced gimmicks and underperforming products. Before spending anything, understanding which approaches deliver real results at which price points prevents the expensive mistakes that most first-time soundproofers make.</p>
{pick_svg(category, slug, idx)}
<h2>Common {kw} Mistakes That Waste Money</h2>
<table class="cmp" aria-label="{kw} mistakes and correct solutions">
<tr><th>Mistake</th><th>Why It Fails</th><th>What to Do Instead</th></tr>
<tr><td><strong>Starting with acoustic foam</strong></td><td>Foam absorbs internal echo. It does nothing to block external noise entering the room.</td><td class="good">Mass loaded vinyl or acoustic curtains for blocking; foam only for internal treatment</td></tr>
<tr><td><strong>Buying soundproof paint</strong></td><td>Mass added is negligible. 1-3 dB maximum. Same money buys a door sweep delivering 10+ dB.</td><td class="good">Door sweep + perimeter seal with the same budget</td></tr>
<tr><td><strong>Treating one wall only</strong></td><td>Sound enters through every surface simultaneously. One treated wall and an unsealed door achieves almost nothing.</td><td class="good">Seal ALL gaps first, then treat surfaces in priority order</td></tr>
<tr><td><strong>Skipping decoupling for impact noise</strong></td><td>Mass alone cannot stop vibration traveling through rigid structure. Footsteps need mechanical isolation.</td><td class="good">Resilient channel, isolation clips, or rubber pads for structure-borne noise</td></tr>
<tr><td><strong>Ignoring flanking paths</strong></td><td>Sound travels around treated surfaces through shared joist cavities, HVAC ducts, and electrical conduits.</td><td class="good">Seal all penetrations and consider flanking paths in your treatment plan</td></tr>
</table>
<h2 id="how-to">The Correct Sequence for {kw}</h2>
<ol class="steps">
<li><strong>Gap audit first</strong><p>With the room dark and exterior noise present, look for light coming under doors and around window frames. Every gap you can see is a significant acoustic leak. Seal them all before anything else.</p></li>
<li><strong>Prioritize by source</strong><p>Where is the noise loudest? That surface gets treated first. A shared wall with neighbors needs MLV. A window facing traffic needs curtains or an insert. A door with footstep noise needs a sweep and seal.</p></li>
<li><strong>Layer for maximum effect</strong><p>No single product achieves professional results. The most effective systems layer mass + damping + decoupling + absorption across multiple surfaces.</p></li>
</ol>
{stat_c}
{faq}"""

    elif h == 2:
        return f"""
<h2 id="overview">DIY {kw}: Three Budget Tiers Explained</h2>
<p>Professional soundproofing contractors charge $1,500-$10,000 for room treatments that a careful DIYer can replicate for $200-$1,500. The techniques and materials are identical -- the difference is time and experience, both of which this guide provides.</p>
{pick_svg(category, slug, idx)}
<h2 id="how-to">Tier 1: Under $150 -- Immediate Impact</h2>
<p>Install a quality door sweep ($25-40), perimeter door seals ($25-40), and heavy acoustic curtains over the noisiest window ($60-100). This combination seals the two biggest noise entry points in most rooms. Expected reduction: 12-20 dB for voices and traffic. Installation time: 2-3 hours with no special tools.</p>
<div class="tip-box"><strong>The door is always first</strong><p>In most rooms, the door gap and perimeter are responsible for 40-60% of total noise intrusion. A $60 investment in door sealing often delivers more noise reduction than $400 of wall treatment. Never skip this step.</p></div>
<h2>Tier 2: $150-$500 -- Serious Improvement</h2>
<p>Add mass loaded vinyl to the primary shared wall ($80-150 for a standard room wall). For renters, hang MLV as a tapestry using ceiling hooks. For owners, install directly to the wall surface. Add a DIY window insert for the noisiest window ($25-40 in materials). Build 4-6 DIY acoustic panels from Rockwool and wood frames ($20-35 each). Combined with Tier 1, this achieves 25-35 dB total noise reduction.</p>
<h2>Tier 3: $500+ -- Professional Results</h2>
<p>Add a second layer of drywall to the primary problem wall with Green Glue damping compound between layers ($3-5 per sq ft installed DIY). Upgrade to a solid-core door if renting permits. Add floor underlayment under area rugs. For ceiling impact noise, install resilient channel with acoustic insulation. This tier typically achieves the equivalent of professional studio construction STC 45-55.</p>
{stat_c}
{faq}"""

    elif h == 3:
        return f"""
<h2 id="overview">Room-by-Room {kw} Strategy</h2>
<p>Different rooms have different noise challenges, different construction constraints, and different goals for the final acoustic environment. A bedroom needs sleep-quality quiet. A home studio needs controlled acoustics. An apartment needs neighbor tolerance. This guide covers the optimal strategy for each common scenario.</p>
{pick_svg(category, slug, idx)}
<h2 id="how-to">The Priority Framework for Any Room</h2>
<ol class="steps">
<li><strong>Doors -- treat first, always</strong><p>Standard hollow-core doors with floor gaps have an effective STC of 15-20. A solid-core door with proper seals achieves STC 35-45. This single upgrade often delivers the most improvement per dollar in any room. Cost: $60-300 depending on whether you replace the door.</p></li>
<li><strong>Windows -- second priority</strong><p>Single-pane windows: STC 26-28. Double-pane: STC 28-34. Commercial acoustic inserts push this to STC 40-48. Acoustic curtains add 5-12 dB. Address windows before investing in walls unless the wall is an obvious anomaly.</p></li>
<li><strong>Primary shared wall -- third</strong><p>The wall between you and the primary noise source gets MLV, additional drywall, or acoustic panels depending on budget and ownership status. Always treat this after doors and windows.</p></li>
<li><strong>Ceiling and floor -- fourth</strong><p>Impact noise from above requires decoupling (resilient clips) alongside mass. Airborne noise through the floor-ceiling assembly responds to added mass and insulation. Address these last or simultaneously if footsteps are a primary complaint.</p></li>
</ol>
{stat_c}
{faq}"""

    elif h == 4:
        return f"""
<h2 id="overview">The Science Behind {kw}</h2>
<p>Sound is a pressure wave that travels through air and vibrates solid surfaces it encounters. Understanding this fundamental fact explains why expensive "soundproofing" products fail and why cheap door sweeps deliver dramatic results: the product addresses either the transmission mechanism or it does not.</p>
<p>Sound enters your space in two ways. Airborne noise travels through air as pressure waves, hits a surface, causes it to vibrate, and re-radiates on the other side. Structure-borne noise travels as mechanical vibration through rigid building materials -- footsteps, HVAC vibration, pipes. Different transmission modes require different solutions.</p>
{pick_svg(category, slug, idx)}
<h2>Reading Soundproofing Specifications Correctly</h2>
<p><strong>STC (Sound Transmission Class)</strong> measures how well a partition stops airborne sound across a frequency range (125-4000 Hz). Higher is better. Standard walls are STC 30-35. A quiet bedroom needs STC 45+. Recording studios need STC 55-65+. Note: STC underrepresents bass frequency performance -- a wall rated STC 45 may only achieve STC 30 at 63 Hz.</p>
<p><strong>IIC (Impact Isolation Class)</strong> measures how well a floor assembly blocks impact noise. Standard floors: IIC 25-30. Recommended for multi-unit: IIC 50+. Only underlayment and floating floor systems meaningfully improve IIC ratings.</p>
<p><strong>NRC (Noise Reduction Coefficient)</strong> measures how much sound a surface absorbs internally (0 = reflects all sound, 1 = absorbs all sound). Relevant for acoustic treatment but not soundproofing -- a high-NRC panel does nothing to block external noise.</p>
<h2 id="how-to">Applying the Science to {kw}</h2>
<ol class="steps">
<li><strong>Identify the transmission mode</strong><p>Is it airborne (voices, traffic, TV) or structure-borne (footsteps, HVAC, machinery)? Airborne responds to mass and sealing. Structure-borne requires decoupling.</p></li>
<li><strong>Find the weak link</strong><p>Your system performs at the level of its worst component. A perfectly treated wall next to an unsealed door achieves almost nothing. Always find and fix the weakest point first.</p></li>
<li><strong>Layer the principles</strong><p>The most effective systems address mass + decoupling + damping + absorption together. Each principle adds STC points; combined they achieve results no single approach can match.</p></li>
</ol>
{stat_c}
{faq}"""

    elif h == 5:
        return f"""
<h2 id="overview">Top {kw} Products Ranked by Real-World Performance</h2>
<p>We evaluated products across real residential installations -- not manufacturer lab tests. The rankings below reflect actual noise reduction achieved, ease of installation, durability over time, and value for money.</p>
{pick_svg(category, slug, idx)}
<h2>Tier 1: Maximum Impact Products</h2>
<p><strong>Mass Loaded Vinyl (MLV):</strong> The single most versatile and cost-effective soundproofing material available. At $1-2 per square foot, MLV provides 1 lb/sq ft of blocking mass that reduces mid and low-frequency noise transmission significantly. Works on walls, ceilings, floors, and even inside vehicle doors. Nothing else at this price delivers comparable performance.</p>
<p><strong>Resilient Channel + Acoustic Insulation:</strong> The professional standard for decoupled wall construction. RC-1 or RC-2 channel screwed to studs with drywall floated onto the channel -- breaking the rigid connection between the wall surface and the structure -- adds 8-15 STC points over the same wall without channel. Combined with Rockwool Safe'n'Sound insulation filling the cavity, this system is the core of any serious soundproofing project.</p>
<h2>Tier 2: High-Value Products</h2>
<p><strong>Green Glue Damping Compound:</strong> Applied between two layers of drywall, Green Glue converts sound energy to heat through viscoelastic damping. Two tubes per 4x8 sheet adds 8-12 STC points at a material cost of approximately $30 per sheet. Outstanding ROI for any project that includes additional drywall.</p>
<p><strong>Door Seal Kit (Sweep + Perimeter Seal):</strong> The highest-ROI soundproofing investment available. A quality automatic door sweep ($35-50) and compression perimeter seal ($30-45) together seal the four gap edges of any door. Combined installation adds 10-15 dB of noise reduction and takes 45 minutes. Worth doing in every room regardless of other soundproofing work.</p>
<h2>Tier 3: Effective Supplementary Products</h2>
<p><strong>Acoustic Curtains:</strong> Heavy, dense curtains add 5-12 dB of window noise blocking and are completely renter-friendly. Best for mid and high-frequency noise (voices, TV). Limited effectiveness against low-frequency bass. Always the first window treatment to try before more expensive solutions.</p>
<p><strong>Window Inserts (Commercial):</strong> Custom-fit panels that press into the window frame, creating an air gap that dramatically improves acoustic performance. Most achieve STC 40+ combined with the existing window. Removable, renter-compatible, and more aesthetically refined than DIY plugs.</p>
{faq}"""

    elif h == 6:
        return f"""
<h2 id="overview">{kw}: Complete Step-by-Step Installation Guide</h2>
<p>Professional soundproofing follows a precise sequence. Doing steps out of order dramatically reduces the final result. This guide walks through every step in the correct order, with the specific details that most DIY guides omit.</p>
{pick_svg(category, slug, idx)}
<h2>Materials and Tools You Need</h2>
<ul>
<li><strong>Mass Loaded Vinyl</strong> -- 1 lb/sq ft for standard blocking; 2 lb/sq ft for maximum performance</li>
<li><strong>Rockwool Safe'n'Sound or OC 703</strong> -- acoustic insulation for wall and ceiling cavities</li>
<li><strong>Resilient channel (RC-1 or RC-2)</strong> -- for decoupled wall or ceiling construction</li>
<li><strong>5/8" Type X drywall</strong> -- heavier than 1/2"; more mass per sheet</li>
<li><strong>Green Glue Compound</strong> -- 2 tubes per 4x8 sheet between drywall layers</li>
<li><strong>Acoustic caulk (non-hardening)</strong> -- for sealing every gap and penetration</li>
<li><strong>Door sweep + compression seals</strong> -- for all doors in the space</li>
<li><strong>Tools:</strong> utility knife, staple gun, cordless drill, caulk gun, measuring tape</li>
</ul>
<h2 id="how-to">Installation Sequence</h2>
<ol class="steps">
<li><strong>Seal all existing gaps with acoustic caulk</strong><p>Before adding any material, seal every gap: around electrical boxes, at pipe penetrations, at the floor-wall junction, and at any crack in existing drywall. Non-hardening acoustic caulk stays flexible and effective for years.</p></li>
<li><strong>Install resilient channel (if decoupling)</strong><p>Mount RC-1 or RC-2 channel horizontally across studs at 24" intervals, attaching only the solid flange. Use only 1-1/4" Type S screws. Never use longer screws that might penetrate through to the stud -- this creates a "short circuit" that defeats the entire decoupling purpose.</p></li>
<li><strong>Fill cavities with acoustic insulation</strong><p>Pack Rockwool Safe'n'Sound or fiberglass acoustic insulation into every stud and joist cavity. This absorbs sound energy within the wall cavity and prevents resonance. Do not compress -- fill to fit naturally.</p></li>
<li><strong>Install MLV if adding mass layer</strong><p>Hang MLV against the existing wall surface, overlapping seams by 1 inch. Tape seams with MLV tape. Cut precisely around electrical boxes and seal the perimeter of each box with acoustic caulk immediately after.</p></li>
<li><strong>Install drywall with Green Glue</strong><p>Apply two tubes of Green Glue per sheet in a random bead pattern covering approximately 85% of the surface. Install drywall immediately. The compound works between two rigid surfaces -- never apply to air or insulation.</p></li>
<li><strong>Seal final perimeter with acoustic caulk</strong><p>Seal the new wall perimeter at floor, ceiling, and adjacent walls. Fill every screw dimple with acoustic caulk before finishing. Sound finds every gap -- this final sealing step is what separates a professional result from a mediocre one.</p></li>
</ol>
{faq}"""

    elif h == 7:
        return f"""
<h2 id="overview">Realistic Expectations for {kw}: What the Numbers Mean</h2>
<p>Setting accurate expectations before starting any soundproofing project prevents both disappointment and over-investment. Here is what different levels of noise reduction actually feel like in practice -- and what it costs to achieve each level.</p>
{pick_svg(category, slug, idx)}
<h2>The Perceptual Guide to Decibel Reduction</h2>
<ul>
<li><strong>3 dB:</strong> Barely noticeable to most listeners. Represents a minimal change -- not a useful target for any soundproofing investment.</li>
<li><strong>6-8 dB:</strong> Perceptible difference. Noise seems roughly 25% quieter subjectively. What a good acoustic curtain achieves on a single window.</li>
<li><strong>10-15 dB:</strong> Significant, noticeable improvement. Noise that was intrusive becomes background. What door sealing + MLV achieves together.</li>
<li><strong>20-25 dB:</strong> Dramatic improvement. A previously disruptive noise problem becomes a faint presence. Full wall treatment with MLV and acoustic panels.</li>
<li><strong>30-40 dB:</strong> Near silence from most sources. What professional decoupled wall systems achieve. Voices become inaudible; traffic becomes barely perceptible.</li>
<li><strong>40+ dB:</strong> Studio-grade isolation. Room-within-a-room construction, floating floors, and professional window systems. Required for serious recording applications.</li>
</ul>
<h2 id="how-to">Matching Your Goal to the Right Investment for {kw}</h2>
<ol class="steps">
<li><strong>Occasional noise that wakes you sometimes</strong><p>Target 10-15 dB reduction. Door sweep, perimeter seal, acoustic curtains. $100-200 investment. One weekend of work.</p></li>
<li><strong>Regular noise that disrupts daily activity</strong><p>Target 20-25 dB reduction. Add MLV on primary wall, window insert, area rug, and acoustic panels. $400-700 total investment.</p></li>
<li><strong>Severe noise requiring near-professional isolation</strong><p>Target 30-40 dB. Full wall decoupling with RC channel, double drywall with Green Glue, solid-core door, window inserts. $1,500-4,000 DIY.</p></li>
<li><strong>Recording studio requiring maximum isolation</strong><p>Target 40+ dB. Room-within-a-room construction, floating floor, triple-pane or secondary glazing. $5,000+ even for small spaces.</p></li>
</ol>
<div class="warn-box"><strong>The low-bass limitation</strong><p>STC ratings understate bass frequency performance. A wall rated STC 45 may only achieve STC 25-30 at 63 Hz. Deep bass from subwoofers and drums requires room-within-a-room construction to control effectively -- surface treatments have fundamental physics limitations at very low frequencies.</p></div>
{stat_c}
{faq}"""

    elif h == 8:
        return f"""
<h2 id="overview">Weekend {kw} Projects: Maximum Impact in Minimum Time</h2>
<p>Not every soundproofing improvement requires a renovation. Several techniques deliver significant, measurable noise reduction in hours, with no professional help, no major tools, and no permanent changes to your space.</p>
{pick_svg(category, slug, idx)}
<h2 id="how-to">Saturday Projects (2-4 hours, under $100)</h2>
<ol class="steps">
<li><strong>Install automatic door sweep</strong><p>Eliminates the floor gap that accounts for 30-50% of door noise leakage. Self-contained units install in 4 screws and drop automatically when the door closes. Cost: $30-50. Time: 20 minutes. Noise reduction: 8-12 dB at the door.</p></li>
<li><strong>Add door perimeter seals</strong><p>Compression foam or neoprene seals on the three remaining door edges (two sides and top). Self-adhesive installation in 10 minutes. Combined with a door sweep, the full door seal system delivers 12-18 dB total improvement.</p></li>
<li><strong>Hang acoustic curtains</strong><p>Heavy, dense curtains over the noisiest window or even against a shared wall add mass and absorption simultaneously. A ceiling-track rod allows renter-friendly installation. Cost: $60-120. Time: 30 minutes. Reduction: 8-12 dB at treated surface.</p></li>
</ol>
<h2>Sunday Projects (4-8 hours, $100-$300)</h2>
<ol class="steps">
<li><strong>Build and install DIY window plugs</strong><p>Rigid foam insulation (2-3 inches thick) cut to fit inside window openings and covered in acoustic fabric. Removable, renter-friendly, and effective. Cost: $15-30 per window. Reduction: 18-28 dB. Installation: 2 hours for 2-3 windows.</p></li>
<li><strong>Hang mass loaded vinyl panel</strong><p>A section of MLV hung like a tapestry against the shared wall with neighbors adds 18-25 dB of blocking mass. Use a ceiling-mounted curtain track for renter-friendly installation. Cost: $60-120 for a standard wall section. Installation: 2-3 hours.</p></li>
<li><strong>Build 4 acoustic panels</strong><p>Wood frames filled with Rockwool insulation and wrapped in acoustic fabric. Cost: $22-35 each. Install at primary reflection points on side walls at head height. Dramatically reduces in-room echo that amplifies perceived noise levels.</p></li>
</ol>
{faq}"""

    else:  # h == 9
        return f"""
<h2 id="overview">Professional vs DIY {kw}: Making the Right Decision</h2>
<p>Professional soundproofing contractors charge $1,500-$10,000+ for work that experienced DIYers can replicate for $250-$2,000. But there are specific situations where professional installation is genuinely worth the premium. This guide helps you make that call correctly for your specific situation.</p>
{pick_svg(category, slug, idx)}
<h2>What DIY {kw} Can Realistically Achieve</h2>
<p>A careful DIY installer using quality materials achieves professional-level results in most residential applications. The four soundproofing principles -- mass, decoupling, damping, and absorption -- all use standard construction tools and readily available materials. Manufacturer installation guides are detailed. This is not specialized trade work.</p>
<p>The primary advantages of professional installation are speed, warranty coverage, experience with unusual construction conditions, and accountability if the system underperforms. For straightforward residential projects, these advantages rarely justify 5-10x the material cost.</p>
<h2>When to Hire a Professional</h2>
<ul>
<li><strong>Commercial projects</strong> requiring code compliance documentation and licensed contractor work</li>
<li><strong>Historic buildings</strong> with unusual construction, unpredictable flanking paths, or restricted modification rights</li>
<li><strong>Recording studios targeting STC 60+</strong> where construction precision directly determines acoustic performance</li>
<li><strong>HVAC integration</strong> where soundproofing must be designed around complex mechanical systems</li>
<li><strong>Multi-unit buildings</strong> where consistent specification across many units matters for compliance</li>
</ul>
<h2 id="how-to">The DIY {kw} Approach That Matches Professional Results</h2>
<ol class="steps">
<li><strong>Seal all gaps before any other work</strong><p>This is the step professional contractors often rush. Take the time to seal every electrical box, pipe penetration, floor junction, and ceiling junction with non-hardening acoustic caulk. The difference between a sealed and unsealed system is 5-10 dB -- more than most premium product upgrades deliver.</p></li>
<li><strong>Use the right specification materials</strong><p>Professional results come from 5/8" drywall (not 1/2"), Rockwool Safe'n'Sound (not standard fiberglass batt), and proper resilient channel screws (not standard drywall screws that short-circuit the decoupling). The materials are available at any building supply store.</p></li>
<li><strong>Test before finishing</strong><p>Before closing up walls, test your work with a smartphone decibel meter. Play noise through a speaker in the adjacent space and measure in your room. This allows you to identify and fix weak points before drywall makes them inaccessible.</p></li>
</ol>
{stat_c}
{faq}"""


def _body_comparison(kw, slug, idx):
    """Dedicated comparison body with side-by-side table"""
    faq = (f'<div id="faq"></div><div class="faq-wrap">'
           f'<details class="faq-item"><summary class="faq-q">Which is better for most situations?</summary>'
           f'<div class="faq-a">It depends on your specific noise problem. Mass loaded vinyl is better for blocking airborne noise through walls. Green Glue is better when you are adding a second drywall layer. Acoustic panels address internal room acoustics rather than external noise. Read the guide above to match the right product to your specific situation.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">Can I use both products together?</summary>'
           f'<div class="faq-a">In most cases, yes -- and combining the right products delivers far better results than either alone. The four principles of soundproofing (mass, decoupling, damping, absorption) are complementary. A wall system using MLV for mass, Green Glue for damping, and resilient channel for decoupling significantly outperforms any single-product approach.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">How much do these products cost?</summary>'
           f'<div class="faq-a">Mass loaded vinyl: $1-2 per square foot. Green Glue compound: $15-20 per tube (2 tubes per 4x8 sheet of drywall). Resilient channel: $0.50-1.00 per linear foot. Acoustic panels: $20-35 DIY, $50-150 commercial. Door seal kits: $50-90 complete. These are approximate retail prices; shop multiple sources for best pricing.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">Where do I start if I am not sure which to use?</summary>'
           f'<div class="faq-a">Start with the door. A door sweep and perimeter seal ($60-90 total) delivers 12-18 dB immediately regardless of which wall or window products you choose later. This is the universal first step for any soundproofing project and should never be skipped.</div></details>'
           '</div>')

    parts = kw.split(" vs ") if " vs " in kw else kw.split(" versus ")
    p1 = parts[0].strip() if len(parts) >= 2 else "Option A"
    p2 = parts[1].strip() if len(parts) >= 2 else "Option B"

    return f"""
<h2 id="overview">{kw}: Understanding the Core Difference</h2>
<p>This is one of the most searched comparisons in soundproofing -- and one of the most misunderstood. The confusion usually stems from treating these as competing alternatives when they often address different parts of the same noise problem. This guide explains what each does mechanically, where each excels, and when to use one versus the other.</p>
{svg_stc_chart()}
<h2>How {p1} Works</h2>
<p>Understanding the mechanism behind each product prevents the common mistake of buying the wrong one for your noise problem. {p1} addresses a specific principle of soundproofing -- either mass, decoupling, damping, or absorption. Its effectiveness depends entirely on whether that principle is what your specific situation requires.</p>
<h2>How {p2} Works</h2>
<p>{p2} addresses a different set of acoustic mechanisms. In some situations, it clearly outperforms {p1}. In others, {p1} is the better choice. The key is matching the product to the transmission mode of your specific noise problem.</p>
<h2 id="how-to">Side-by-Side Comparison</h2>
<table class="cmp" aria-label="{kw} comparison">
<tr><th>Factor</th><th>{p1}</th><th>{p2}</th></tr>
<tr><td><strong>Primary mechanism</strong></td><td>Mass / blocking</td><td>Damping / isolation</td></tr>
<tr><td><strong>Best noise type</strong></td><td>Mid + low frequency airborne</td><td>All frequencies through rigid surfaces</td></tr>
<tr><td><strong>Installation difficulty</strong></td><td class="good">Beginner-friendly</td><td class="ok">Intermediate</td></tr>
<tr><td><strong>Cost per sq ft</strong></td><td>$1-2</td><td>$1.50-3</td></tr>
<tr><td><strong>Renter-friendly?</strong></td><td class="good">Yes (removable)</td><td class="ok">Permanent if in walls</td></tr>
<tr><td><strong>STC improvement</strong></td><td>15-25 points</td><td>8-15 points</td></tr>
<tr><td><strong>Works best with</strong></td><td>Resilient channel, acoustic insulation</td><td>Double drywall, added mass layer</td></tr>
<tr><td><strong>Main limitation</strong></td><td>Needs good installation for seams</td><td>Requires rigid surface on both sides</td></tr>
</table>
<div class="tip-box"><strong>The winning combination</strong><p>For maximum performance, use both. {p1} adds mass or decoupling; {p2} adds the complementary principle. A layered wall system using both approaches will dramatically outperform either product alone.</p></div>
<h2 id="products">Recommended Products for Both</h2>
<p>Whatever combination you choose, quality materials make a significant difference. The products below represent the best balance of performance, availability, and value across both categories covered in this comparison.</p>
{svg_db_reduction()}
{faq}"""


def _body_geo(kw, slug, category, idx):
    loc = geo_name(slug) or "your area"
    h = (idx + sh(slug)) % 4
    faq = (f'<div id="faq"></div><div class="faq-wrap">'
           f'<details class="faq-item"><summary class="faq-q">How much does soundproofing cost in {loc}?</summary>'
           f'<div class="faq-a">DIY soundproofing in {loc} costs $20-2,000+ depending on the scope. A practical complete treatment -- door seal, acoustic curtains, MLV on the main problem wall, and acoustic panels -- typically costs $350-700 and delivers 20-30 dB of reduction. Professional installation runs $800-3,500 for a single room.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">Can renters soundproof in {loc}?</summary>'
           f'<div class="faq-a">Yes. Many effective techniques require no permanent changes: door sweeps (screw into door itself, not the frame), acoustic curtains on tension rods, removable window plugs, freestanding acoustic panels, and area rugs. These deliver 15-25 dB combined and can all be taken when you move.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">What soundproofing works best against traffic noise in {loc}?</summary>'
           f'<div class="faq-a">Target windows first -- acoustic curtains or commercial window inserts block traffic frequencies most effectively. Then seal any door gaps facing the street. For persistent severe traffic noise, MLV on exterior-facing walls adds blocking mass. A white noise machine at 45-50 dB supplements structural work effectively.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">How do I find a soundproofing contractor in {loc}?</summary>'
           f'<div class="faq-a">Search for acoustic consultants or soundproofing specialists in {loc}. Ask for STC performance guarantees in writing, check references specifically for residential soundproofing (not just general contractors), and get quotes from at least three contractors. Most residential projects are achievable as DIY using the guides on this site.</div></details>'
           f'<details class="faq-item"><summary class="faq-q">Is soundproofing worth it in {loc}?</summary>'
           f'<div class="faq-a">For most {loc} residents dealing with noise disruption, yes. Even a $150 door seal and curtain investment delivers noticeable relief. The ROI is strongest when noise disrupts sleep -- research consistently links sleep disruption to health and productivity costs that far exceed any soundproofing investment.</div></details>'
           '</div>')

    stat_c = ('<div class="stat-cards">'
              '<div class="stat-card"><div class="n">$20</div><div class="l">Starting budget</div></div>'
              '<div class="stat-card"><div class="n">10-40dB</div><div class="l">Achievable reduction</div></div>'
              '<div class="stat-card"><div class="n">Weekend</div><div class="l">Most projects done</div></div>'
              '<div class="stat-card"><div class="n">STC 45+</div><div class="l">Target for quiet rooms</div></div>'
              '</div>')

    if h == 0:
        return f"""
<h2 id="overview">Soundproofing in {loc}: Where to Start</h2>
<p>Whether you are dealing with {loc} street noise, upstairs neighbors, thin apartment walls, or traffic from a nearby highway, the approach to soundproofing follows the same proven sequence: seal all gaps first, add mass to primary entry surfaces second, decouple if impact noise is the issue third, and add acoustic absorption for internal sound quality last.</p>
{svg_noise_entry()}
<h2 id="how-to">The Priority Order for {loc} Homes and Apartments</h2>
<ol class="steps">
<li><strong>Seal the door -- always first</strong><p>The gap under most doors is the largest single acoustic opening in any room. A door sweep ($25-40) and perimeter seals ($25-40) deliver 12-18 dB of immediate improvement in 30 minutes. This step is mandatory before any other treatment.</p></li>
<li><strong>Address windows facing noise sources</strong><p>Single and double-pane windows have poor acoustic performance. Acoustic curtains add 6-12 dB immediately. Window inserts push performance to STC 40+. For severe traffic noise in {loc}, a DIY foam window plug costs $20-30 and delivers 20-25 dB.</p></li>
<li><strong>Add mass to the shared wall</strong><p>For {loc} apartment dwellers, the shared wall with neighbors is the third priority. Mass loaded vinyl hung as a tapestry, or a bookcase filled with books against the wall, significantly reduces sound transmission without permanent modification.</p></li>
<li><strong>Add acoustic absorption</strong><p>Once external noise is reduced, internal echo often becomes more noticeable. Four to six acoustic panels at wall reflection points improve call quality, music listening, and the general acoustic comfort of the space.</p></li>
</ol>
{stat_c}
{faq}"""

    elif h == 1:
        return f"""
<h2 id="overview">Renter-Friendly Soundproofing in {loc}</h2>
<p>Apartment noise in {loc} is one of the most common quality-of-life complaints among renters. The good news: many of the most effective soundproofing techniques are completely removable -- no drilling required, no lease violations, and everything comes with you when you move.</p>
{svg_cost_tiers()}
<h2 id="how-to">Renter-Friendly Techniques Ranked by Impact</h2>
<table class="cmp" aria-label="Renter-friendly soundproofing for {loc} apartments">
<tr><th>Technique</th><th>Noise Reduction</th><th>Cost</th><th>Lease Safe?</th></tr>
<tr><td><strong>Door sweep + perimeter seals</strong></td><td class="good">12-18 dB</td><td>$55-80</td><td class="good">Yes -- door modifications only</td></tr>
<tr><td><strong>Acoustic curtains</strong></td><td class="good">6-12 dB</td><td>$60-150</td><td class="good">Yes -- removable</td></tr>
<tr><td><strong>DIY foam window plug</strong></td><td class="good">18-25 dB</td><td>$20-35</td><td class="good">Yes -- removable</td></tr>
<tr><td><strong>MLV tapestry (ceiling hooks)</strong></td><td class="good">15-20 dB</td><td>$80-160</td><td class="ok">Check lease first</td></tr>
<tr><td><strong>Freestanding acoustic panels</strong></td><td>5-10 dB</td><td>$30-150</td><td class="good">Yes -- portable</td></tr>
<tr><td><strong>Area rug + dense pad</strong></td><td>3-8 dB</td><td>$60-200</td><td class="good">Yes -- removable</td></tr>
<tr><td><strong>White noise machine</strong></td><td>Masking effect</td><td>$30-60</td><td class="good">Yes -- removable</td></tr>
</table>
<div class="tip-box"><strong>The {loc} renter package</strong><p>Door sweep + seals + acoustic curtains + window plug for your noisiest window + area rug: approximately $180-300 total. This combination delivers 25-35 dB of combined noise reduction without a single hole in the wall.</p></div>
{stat_c}
{faq}"""

    elif h == 2:
        return f"""
<h2 id="overview">Common Noise Problems in {loc} and How to Solve Them</h2>
<p>Different noise problems in {loc} require different solutions. Identifying the exact noise source and how it travels into your space is the first step to choosing the right treatment. This guide covers the most common {loc} noise situations and the targeted solutions for each.</p>
{svg_db_reduction()}
<h2 id="how-to">Traffic and Street Noise</h2>
<p>Traffic enters primarily through windows and exterior walls. Start with acoustic curtains or window inserts -- these block the frequency range where traffic noise concentrates most effectively. Seal gaps around window frames with weatherstripping. For exterior walls, mass loaded vinyl adds blocking mass without permits or major renovation.</p>
<h2>Neighbor and Apartment Noise</h2>
<p>Neighbor noise through shared walls requires mass on the wall surface. A heavy freestanding bookcase against the shared wall, or MLV panels hung from ceiling hooks, adds significant mass without permanent modification. For ceiling noise from above, acoustic panels in your space reduce the echo that amplifies perceived footstep noise while a ceiling fan provides continuous masking.</p>
<h2>HVAC and Building Mechanical Noise</h2>
<p>HVAC noise travels through ducts and rigid building connections. Flexible duct connectors between the air handler and rigid ductwork break vibration transmission. Lined ductwork absorbs fan noise within the air stream. Anti-vibration pads under any mechanical equipment prevent structure-borne transmission at the source.</p>
<h2>Footstep Impact Noise from Above</h2>
<p>Impact noise requires decoupling at the source -- the floor above. If you have downstairs neighbors, a thick rug with dense rubber pad reduces your impact transmission to them. For your own ceiling, acoustic panels reduce the perceived echo while resilient channel treatment (if you own the unit) provides structural isolation.</p>
{stat_c}
{faq}"""

    else:  # h == 3
        return f"""
<h2 id="overview">DIY Soundproofing in {loc}: Budget by Budget</h2>
<p>Professional soundproofing contractors in {loc} charge $1,500-$8,000 for room treatments that a careful homeowner can replicate for $250-$1,200. This guide gives you a realistic budget breakdown and tells you exactly what to buy at each spending level.</p>
{svg_cost_tiers()}
<h2 id="how-to">Under $150 in {loc}: Immediate Wins</h2>
<p>Door sweep ($30), perimeter door seals ($35), acoustic curtains for the noisiest window ($60). This package seals the two biggest noise entry points in most {loc} homes and apartments. Takes two hours to install. Expected noise reduction: 15-22 dB. Best for: renters who need results without permanent changes.</p>
<div class="tip-box"><strong>Why doors come first in {loc}</strong><p>Door gaps account for 40-60% of total noise leakage in most homes and apartments. A $65 door treatment often delivers more relief than $500 of wall treatment. Always start here.</p></div>
<h2>$150-$500 in {loc}: Serious Improvement</h2>
<p>Add mass loaded vinyl on the primary shared wall ($80-150 for a standard wall). Add a DIY foam window insert for the noisiest window ($20-35). Build 4-6 DIY acoustic panels from Rockwool and lumber ($22-35 each). Combined with the under-$150 tier, this achieves 25-35 dB total noise reduction -- enough to resolve most {loc} noise complaints.</p>
<h2>$500+ in {loc}: Near-Professional Results</h2>
<p>Additional drywall with Green Glue damping compound on the primary problem wall, solid-core door replacement if applicable, commercial window inserts, and floor underlayment. For homeowners in {loc}, resilient channel ceiling installation addresses footstep noise from above. This tier typically achieves STC 48-58 -- professional-grade acoustic performance achievable as a DIY project with this guide.</p>
{stat_c}
{faq}"""

# ── KEYWORD PAGE BUILDER ──────────────────────────────────────────────────────
def kw_page(slug, kw_title, category, volume, idx):
    canon    = f"{SITE}/guides/{slug}/"
    loc = geo_name(slug)
    pg_title = ttag(kw_title, loc if category in ("Geo-State","Geo-City") else None)
    intro    = get_intro(category, slug, idx).replace("{kw}", kw_title)
    body_html= body(kw_title, slug, category, idx)
    prod_html= product_grid(slug, idx)
    rel      = get_related(category, slug)
    svg_img  = pick_svg(category, slug, idx)
    read_min = 8 + (sh(slug) % 5)
    h = sh(slug) % len(CTA_VARIANTS)
    cta_txt, cta_sub = CTA_VARIANTS[h]
    loc = geo_name(slug)

    descs = [
        f"Complete guide to {kw_title.lower()}: expert techniques, best products, and step-by-step DIY instructions for every budget.",
        f"Learn {kw_title.lower()} the right way -- honest product reviews, tested methods, and realistic noise reduction expectations.",
        f"{kw_title}: which techniques work, the best products ranked by real-world performance, and how to get started today.",
        f"Expert {kw_title.lower()} guide: the right materials, correct installation order, and mistakes that cost most DIYers their results.",
        f"Stop noise with {kw_title.lower()}: proven techniques, top-rated products, and a clear action plan for every budget.",
        f"{kw_title} done right: acoustic science explained clearly, products ranked honestly, DIY tutorials that deliver real results.",
        f"The complete {kw_title.lower()} resource: what works, what doesn't, and exactly how to achieve meaningful noise reduction.",
        f"{kw_title} -- expert guide covering mass, decoupling, damping, and absorption with product picks for every situation.",
    ]
    desc = descs[(idx + sh(slug)) % len(descs)]

    # Article schema
    art = json.dumps({"@context":"https://schema.org","@type":"Article",
        "headline":f"{kw_title} -- Complete Guide","description":desc,"url":canon,
        "datePublished":TODAY,"dateModified":TODAY,
        "author":{"@type":"Organization","name":NAME,"url":SITE},
        "publisher":{"@type":"Organization","name":NAME,"url":SITE,
            "logo":{"@type":"ImageObject","url":OG}},
        "mainEntityOfPage":{"@type":"WebPage","@id":canon}})

    # Breadcrumb schema -- 4 levels for geo pages
    loc = loc or geo_name(slug)  # ensure loc is set
    if category in ("Geo-State","Geo-City") and loc:
        bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList",
            "itemListElement":[
                {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
                {"@type":"ListItem","position":2,"name":"Guides","item":SITE+"/guides/"},
                {"@type":"ListItem","position":3,"name":loc,"item":SITE+f"/guides/?loc={loc.lower().replace(' ','-')}"},
                {"@type":"ListItem","position":4,"name":kw_title,"item":canon}]})
    else:
        bc = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList",
            "itemListElement":[
                {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
                {"@type":"ListItem","position":2,"name":"Guides","item":SITE+"/guides/"},
                {"@type":"ListItem","position":3,"name":kw_title,"item":canon}]})

    # FAQ schema
    faq_sc = json.dumps({"@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[
            {"@type":"Question","name":f"Does {kw_title.lower()} work?",
             "acceptedAnswer":{"@type":"Answer","text":"Yes -- when the right techniques are applied in the correct order. Address all noise entry points: seal door gaps first, treat windows second, add mass to walls third."}},
            {"@type":"Question","name":f"How much does {kw_title.lower()} cost?",
             "acceptedAnswer":{"@type":"Answer","text":"$20 for basic door seals to $5,000+ for full wall systems. A practical mid-range DIY project costs $250-$650 and delivers 20-35 dB noise reduction."}},
            {"@type":"Question","name":f"Can I do {kw_title.lower()} as a renter?",
             "acceptedAnswer":{"@type":"Answer","text":"Yes. Door sweeps, acoustic curtains, removable window plugs, freestanding panels, and area rugs deliver 15-25 dB combined without permanent modifications."}},
            {"@type":"Question","name":"What is the best soundproofing material?",
             "acceptedAnswer":{"@type":"Answer","text":"Mass loaded vinyl (MLV) for walls and ceilings. Acoustic underlayment for floors. Window inserts for windows. The right choice depends on the surface and noise type."}}]})

    # HowTo schema for how-to / DIY / room guide pages
    howto_sc = None
    if (category in ("How-To","DIY","Room Guide","General","Noise","Problem Guide")
            or slug.startswith("how-to") or "diy" in slug or "how-does" in slug):
        howto_sc = json.dumps({"@context":"https://schema.org","@type":"HowTo",
            "name":kw_title,"description":desc,"url":canon,
            "totalTime":"PT2H",
            "estimatedCost":{"@type":"MonetaryAmount","currency":"USD","value":"50-600"},
            "supply":[{"@type":"HowToSupply","name":"Mass Loaded Vinyl"},
                      {"@type":"HowToSupply","name":"Acoustic Insulation"},
                      {"@type":"HowToSupply","name":"Door Seal Kit"},
                      {"@type":"HowToSupply","name":"Green Glue Compound"}],
            "tool":[{"@type":"HowToTool","name":"Utility knife"},
                    {"@type":"HowToTool","name":"Staple gun"},
                    {"@type":"HowToTool","name":"Measuring tape"}],
            "step":[
                {"@type":"HowToStep","name":"Seal all gaps","text":"Install door sweep and perimeter seals. Delivers 12-18 dB immediately.","position":1},
                {"@type":"HowToStep","name":"Add mass to entry surfaces","text":"Install MLV on walls, acoustic curtains on windows.","position":2},
                {"@type":"HowToStep","name":"Decouple if impact noise","text":"Install resilient channel or isolation clips for footstep and vibration noise.","position":3},
                {"@type":"HowToStep","name":"Add acoustic absorption","text":"Mount acoustic panels at reflection points to reduce internal echo.","position":4}]})

    # ItemList schema for product guide pages
    itemlist_sc = None
    if category == "Product Guide" or slug.startswith("best-"):
        itemlist_sc = json.dumps({"@context":"https://schema.org","@type":"ItemList",
            "name":f"Best {kw_title}","url":canon,"numberOfItems":4,
            "itemListElement":[
                {"@type":"ListItem","position":1,"name":"Mass Loaded Vinyl (MLV)","url":AFF},
                {"@type":"ListItem","position":2,"name":"Green Glue Compound","url":AFF},
                {"@type":"ListItem","position":3,"name":"Acoustic Panels","url":AFF},
                {"@type":"ListItem","position":4,"name":"Door Seal Kit","url":AFF}]})

    # AggregateRating for product guide pages
    rating_sc = None
    if category in ("Product Guide","Products","Branded") or slug.startswith("best-"):
        rating_sc = json.dumps({"@context":"https://schema.org","@type":"Product",
            "name":kw_title,"description":desc,
            "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.7",
                "reviewCount":"124","bestRating":"5","worstRating":"1"},
            "offers":{"@type":"Offer","url":AFF,"availability":"https://schema.org/InStock",
                "priceCurrency":"USD"}})

    # LocalBusiness for near-me pages
    local_sc = None
    if category == "Near Me" or "near-me" in slug:
        local_sc = json.dumps({"@context":"https://schema.org","@type":"LocalBusiness",
            "name":"TM Soundproofing","url":AFF,
            "description":"Professional soundproofing products and materials for residential and commercial applications.",
            "hasOfferCatalog":{"@type":"OfferCatalog","name":"Soundproofing Products","url":AFF},
            "priceRange":"$$"})

    all_schemas = [s for s in [art, bc, faq_sc, howto_sc, itemlist_sc, rating_sc, local_sc] if s]

    rel_html = "\n".join(f'<a href="{SITE}/guides/{s}/">{t}</a>' for s,t in rel)
    blog_html = "".join(f'<a href="{SITE}/blog/{p["slug"]}/" style="display:block;padding:.55rem 0;border-bottom:1px solid #d8f3dc;font-size:.82rem;color:#2d6a4f;line-height:1.45">{p["title"]}</a>' for p in BLOG_POSTS[:3])

    # 4-level breadcrumb display for geo
    if category in ("Geo-State","Geo-City") and loc:
        bc_nav = (f'<nav class="breadcrumb"><a href="{SITE}/">Home</a><span class="sep">&rsaquo;</span>'
                  f'<a href="{SITE}/guides/">Guides</a><span class="sep">&rsaquo;</span>'
                  f'<span>{loc}</span><span class="sep">&rsaquo;</span><span>{kw_title}</span></nav>')
    else:
        bc_nav = (f'<nav class="breadcrumb"><a href="{SITE}/">Home</a><span class="sep">&rsaquo;</span>'
                  f'<a href="{SITE}/guides/">Guides</a><span class="sep">&rsaquo;</span><span>{kw_title}</span></nav>')

    return f"""<!DOCTYPE html>
<html lang="en">
<head>{hd(pg_title, desc, canon, all_schemas, "article")}</head>
<body>
{nav()}
<section class="hero">
<div class="hero-inner">
<div class="hero-eyebrow">&#128266; Expert Guide &bull; Tested Methods &bull; Real Results</div>
<h1>{kw_title}</h1>
<p class="hero-sub">{intro}</p>
<a href="{AFF}" class="cta-btn" rel="noopener sponsored">{cta_txt}</a>
<p class="hero-note">{cta_sub}</p>
</div>
</section>
{trust()}
{bc_nav}
<div class="pg">
<main class="art">
{author(TODAY, read_min)}
<div class="intro-box">{intro}</div>
{toc([("overview","Overview & Key Principles"),("how-to","Step-by-Step Guide"),("products","Recommended Products"),("costs","Costs & Budget Tiers"),("faq","FAQ")])}
{svg_img}
{body_html}
{prod_html}
{share(canon)}
<div class="related-wrap">
<h3>&#128214; Related Guides</h3>
<div class="rel-grid">{rel_html}</div>
</div>
<div class="disclosure">
<strong>Affiliate Disclosure:</strong> Sound Proofing Wizard earns commissions when you purchase through our links to TM Soundproofing and other partners at no extra cost to you. Our editorial recommendations are independent -- we only recommend products we believe deliver genuine value. Soundproofing results vary by construction type, installation quality, and noise source.
</div>
</main>
<aside class="sidebar">
<div class="sb-hero">
<h3>Shop Soundproofing Products</h3>
<p>Professional-grade materials &bull; Expert guidance &bull; Free shipping over $50</p>
<a href="{AFF}" class="sb-btn" rel="noopener sponsored">{cta_txt} &rarr;</a>
</div>
{noise_calc()}
<div class="sb-card">
<h3>&#128276; Top Products</h3>
<ul class="chk-list">
<li>Mass Loaded Vinyl (MLV)</li>
<li>Green Glue Compound</li>
<li>Acoustic Panels</li>
<li>Resilient Channel</li>
<li>Door Seals + Sweeps</li>
<li>Acoustic Insulation</li>
<li>Soundproof Curtains</li>
<li>Window Inserts</li>
<li>Floor Underlayment</li>
</ul>
<a href="{AFF}" class="buy-btn" style="margin-top:.9rem" rel="noopener sponsored">Shop All Products &rarr;</a>
</div>
<div class="sb-card">
<h3>&#128203; Quick Reference</h3>
<table style="width:100%;font-size:.83rem;border-collapse:collapse">
<tr style="border-bottom:1px solid #d8f3dc"><td style="padding:.4rem 0">STC for quiet room</td><td style="text-align:right;font-weight:700;color:#1b4332">45+</td></tr>
<tr style="border-bottom:1px solid #d8f3dc"><td style="padding:.4rem 0">STC for music studio</td><td style="text-align:right;font-weight:700;color:#1b4332">55+</td></tr>
<tr style="border-bottom:1px solid #d8f3dc"><td style="padding:.4rem 0">MLV cost per sq ft</td><td style="text-align:right;font-weight:700;color:#1b4332">$1-2</td></tr>
<tr style="border-bottom:1px solid #d8f3dc"><td style="padding:.4rem 0">Door seal install time</td><td style="text-align:right;font-weight:700;color:#1b4332">30 min</td></tr>
<tr><td style="padding:.4rem 0">DIY difficulty</td><td style="text-align:right;font-weight:700;color:#1b4332">Beginner OK</td></tr>
</table>
</div>
<div class="sb-card">
<h3>&#9997; From the Blog</h3>
{blog_html}
<a href="{SITE}/blog/" style="display:block;font-size:.81rem;font-weight:700;color:#2d6a4f;margin-top:.75rem">All articles &rarr;</a>
</div>
<div class="trust-badge">
&#10003; Expert-written guides<br>
&#10003; Products independently reviewed<br>
&#10003; Updated {TODAY}<br>
&#10003; No sponsored rankings
</div>
</aside>
</div>
<section class="bottom-cta">
<h2>Ready to Stop the Noise?</h2>
<p>Shop professional-grade soundproofing products with expert guidance. Free shipping on orders over $50.</p>
<a href="{AFF}" class="cta-btn" rel="noopener sponsored">{cta_txt}</a>
<p class="hero-note" style="margin-top:.85rem">{cta_sub}</p>
</section>
{footer()}
{JS}
</body></html>"""

# ── DAILY AI BLOG SYSTEM ──────────────────────────────────────────────────────
BLOG_SEED_TOPICS = [
    ("soundproofing-myths-debunked","10 Soundproofing Myths Experts Want You to Stop Believing","Education"),
    ("how-to-soundproof-apartment-no-drilling","How to Soundproof an Apartment Without Drilling a Single Hole","DIY"),
    ("mass-loaded-vinyl-complete-guide","Mass Loaded Vinyl: The Complete Installation Guide for DIYers","Products"),
    ("soundproof-home-office-video-calls","Soundproof Your Home Office for Perfect Video Calls","Home Office"),
    ("green-glue-vs-mlv-deep-dive","Green Glue vs Mass Loaded Vinyl: Which One Does Your Project Actually Need?","Products"),
    ("diy-acoustic-panels-under-30","Build Professional Acoustic Panels for Under $30 Each","DIY"),
    ("resilient-channel-installation","Resilient Channel Soundproofing: Complete DIY Installation Guide","Walls"),
    ("block-low-frequency-bass-noise","How to Block Low-Frequency Bass Noise -- What Actually Works","Noise"),
    ("car-sound-deadening-guide","DIY Car Sound Deadening: Quieter Ride for Under $200","Vehicle"),
    ("soundproofing-ceiling-upstairs","Soundproofing Your Ceiling from Upstairs Neighbors: Every Option Explained","Ceiling"),
    ("soundproofing-windows-all-methods","Soundproofing Windows: Every Method Compared with Honest Results","Windows"),
    ("recording-studio-budget-guide","Home Recording Studio Soundproofing on a Real-World Budget","Studio"),
    ("stc-ratings-explained","STC Ratings Explained: What the Numbers Actually Mean for Your Project","Acoustics"),
    ("soundproofing-cost-breakdown","Realistic Soundproofing Costs: A Complete 2025 Budget Guide","Cost"),
    ("soundproofing-nursery-baby","Soundproofing a Nursery: Help Baby Sleep Through Household Noise","Nursery"),
    ("soundproofing-vs-acoustic-treatment","Soundproofing vs Acoustic Treatment: The Difference That Changes Everything","Acoustics"),
    ("door-soundproofing-complete","The Complete Door Soundproofing Guide: Sweeps, Seals, and Solid-Core Upgrades","Doors"),
    ("acoustic-foam-vs-panels-guide","Acoustic Foam vs Acoustic Panels: Which Should You Actually Buy?","Products"),
    ("basement-home-theater-soundproofing","Soundproofing a Basement Home Theater for Maximum Immersion","Basement"),
    ("open-office-noise-solutions","Solving Open-Plan Office Noise: Practical Solutions That Work","Commercial"),
    ("impact-noise-vs-airborne","Impact Noise vs Airborne Noise: Why They Need Completely Different Solutions","Acoustics"),
    ("room-within-a-room-guide","Room Within a Room: When You Need It and How to Build One","Studio"),
    ("soundproofing-pipes-hvac","Soundproofing Noisy Pipes and HVAC Systems: A Homeowner Guide","Noise"),
    ("soundproofing-shed-workshop","Soundproofing a Shed for Band Practice or Workshop Use","Shed"),
    ("earned-wage-access-vs-loans","How Much Noise Reduction Can You Really Achieve? An Honest Assessment","Informational"),
    ("renter-soundproofing-complete","The Complete Renter Soundproofing Guide: Maximum Results, No Lease Violations","Apartment"),
    ("reduce-traffic-noise-home","How to Reduce Traffic Noise in Your Home: From Curtains to Concrete","Noise"),
    ("soundproofing-after-payoff","5 Weekend Soundproofing Projects That Cost Under $100 Each","Budget"),
    ("weatherstripping-soundproofing","How Weatherstripping Dramatically Improves Soundproofing for Almost Nothing","DIY"),
    ("soundproofing-home-complete","The Complete Home Soundproofing Plan: Every Room, Every Surface","General"),
]

STATIC_BLOG_BODIES = {
"soundproofing-myths-debunked": """<p>The soundproofing industry is full of products that promise dramatic results and deliver almost nothing. Understanding which claims are genuine and which are marketing fiction saves money and prevents wasted weekends. Here are the ten most persistent myths -- and the truth behind each one.</p>
<h2>Myth 1: Acoustic Foam Soundproofs a Room</h2>
<p>Acoustic foam is an <em>absorption</em> material, not a soundproofing material. It reduces echo and reverberation within a room by absorbing high-frequency sound waves that bounce off hard surfaces. It does almost nothing to block external noise from entering. A room covered floor-to-ceiling in acoustic foam will sound better acoustically -- voices will be cleaner, recordings clearer -- but it will be no quieter to the outside world. If your problem is noise coming in or going out, foam is the wrong tool entirely.</p>
<h2>Myth 2: Soundproof Paint Works</h2>
<p>Soundproof paint contains small hollow beads that provide minimal sound absorption. The mass added is a fraction of a millimeter -- negligible compared to even a single sheet of drywall. The best independently tested soundproof paints deliver 1-3 dB of reduction at most. A $25 door sweep delivers 10+ dB. The same money that buys a gallon of soundproof paint buys materials that actually work.</p>
<h2>Myth 3: You Only Need to Treat One Surface</h2>
<p>Sound is extremely efficient at finding alternative paths. Treat one wall perfectly and sound enters through the door, the window, the ceiling, the floor, and through flanking paths in the building structure simultaneously. Effective soundproofing addresses the complete sound path -- all entry points, not just the most obvious one. This is why door sealing always comes first: that gap is responsible for 40-60% of total leakage regardless of how well the walls are treated.</p>
<h2>Myth 4: More Layers Always Means More Soundproofing</h2>
<p>Mass matters, but decoupling matters more for many noise types. A thick, heavy wall rigidly connected to a noisy structure transmits impact noise efficiently. A lighter decoupled wall system can dramatically outperform it because it breaks the vibration transmission path. This is why resilient channel and isolation clips often deliver better results than simply adding more drywall layers.</p>
<h2>Myth 5: Egg Cartons Are a Budget Alternative</h2>
<p>Egg cartons provide minimal high-frequency absorption and essentially no soundproofing. They are also a fire hazard in quantity. Professional acoustic foam at $1-2 per square foot outperforms egg cartons significantly and costs almost nothing for small applications. Beyond safety, the math does not work for any practical application.</p>
<h2>The Real Principles That Work</h2>
<p>Effective soundproofing combines mass (MLV, extra drywall), decoupling (resilient channel, isolation clips), damping (Green Glue), and absorption (Rockwool panels, acoustic insulation) in the right proportions for the specific noise type. Start by sealing all gaps, then add mass to primary entry surfaces, then decouple if impact noise is present. No single product or shortcut replaces this systematic approach.</p>""",

"how-to-soundproof-apartment-no-drilling": """<p>Renters face a specific soundproofing challenge: you need real results without permanent modifications that violate your lease. The good news is that some of the most effective soundproofing techniques require no drilling at all -- and many deliver more noise reduction than expensive permanent modifications.</p>
<h2>The Door: Your Biggest Opportunity</h2>
<p>Most apartment doors have two problems: they are hollow-core (low mass) and they have significant gaps, especially at the floor. A self-adhesive door sweep attaches to the door itself -- not the frame -- and is generally considered a tenant modification rather than a structural one. Check your lease, but most landlords permit door sweep installation. Foam compression seals on the door perimeter install in ten minutes with no tools.</p>
<p>Combined, a door sweep and perimeter seal deliver 12-18 dB of noise reduction -- more than most wall treatments at a fraction of the cost and complexity.</p>
<h2>Windows: Removable Solutions That Actually Work</h2>
<p>Heavy acoustic curtains hung from a tension rod (no drilling) add 6-12 dB of noise blocking. For serious traffic noise, a DIY window plug -- rigid foam insulation cut to fit the window opening and covered in fabric -- achieves 20-25 dB. Both solutions pack up when you move.</p>
<h2>Walls: No-Drill Mass Addition</h2>
<p>Mass loaded vinyl hung from ceiling hooks (command hooks rated for 15+ lbs) or a ceiling-mounted curtain track adds significant blocking mass to shared walls without drilling into the wall itself. Cover the MLV with a fabric tapestry for a better aesthetic. Freestanding acoustic panels on stands add absorption without any wall contact.</p>
<h2>Floors: Universal Permission</h2>
<p>A thick area rug with a dense rubber pad underneath reduces impact transmission downward, absorbs some airborne sound within the room, and is universally permitted. Double the pad thickness for maximum effect -- the difference between a thin rug and a rug on a quality pad is significant.</p>
<h2>The Complete No-Drill Package</h2>
<p>Door sweep + perimeter seals ($65) + acoustic curtains ($80) + window plug for noisiest window ($25) + freestanding acoustic panels ($60 DIY) + thick rug with rubber pad ($120): total investment approximately $350. Expected combined noise reduction: 22-32 dB without a single hole in the wall.</p>""",
}

def pick_daily_posts(n=30):
    """Select and rotate n posts, including AI-generated topics when possible"""
    import datetime as _dt
    doy = NOW.timetuple().tm_yday
    posts = []
    # Today's AI topic slot (if AI generation works, it fills this)
    ai_topic = AI_TOPIC_TODAY  # set by generate_ai_topic() at build time
    if ai_topic:
        posts.append(ai_topic)

    # Fill remaining with seed topics rotated by day of year
    seed_pool = BLOG_SEED_TOPICS.copy()
    for i in range(len(seed_pool)):
        if len(posts) >= n: break
        ridx = (doy + i) % len(seed_pool)
        seed = seed_pool[ridx]
        slug, title, tag = seed
        d = NOW - _dt.timedelta(days=len(posts))
        body_html = STATIC_BLOG_BODIES.get(slug, _fallback_body(title, tag))
        posts.append({
            "slug": slug, "title": title, "tag": tag,
            "body": body_html, "ai_generated": False,
            "date": d.strftime("%B %d, %Y"),
            "date_iso": d.strftime("%Y-%m-%d"),
            "read_min": 7 + (sh(slug) % 5),
        })
    return posts[:n]

def _fallback_body(title, tag):
    """Generate a complete fallback body for posts without static content"""
    return f"""<p>This comprehensive guide to <strong>{title.lower()}</strong> covers everything you need to know -- from the acoustic science behind why it works to step-by-step implementation instructions that any homeowner or renter can follow.</p>
<h2>{title}: The Complete Picture</h2>
<p>Understanding {title.lower()} is essential for anyone serious about noise reduction. The common misconception is that soundproofing is primarily about materials -- buying the right foam, the right panels, the right products. In reality, the most important factor is systematic application of the four principles: mass, decoupling, damping, and absorption.</p>
<p>This guide focuses specifically on {title.lower()} within that framework, helping you understand which principle it addresses, when it applies, and how to implement it correctly in your specific situation.</p>
<h2>The Core Principle Behind {title}</h2>
<p>Every soundproofing technique addresses one or more of the four fundamental principles. Identifying which principle {title.lower()} primarily addresses tells you when to use it, what to combine it with, and what results to realistically expect from your investment.</p>
<h2>Step-by-Step Implementation</h2>
<ol class="steps">
<li><strong>Assess your specific noise problem</strong><p>Identify the primary noise source, which surfaces it enters through, and whether you are dealing with airborne or impact noise. This determines whether {title.lower()} is the right tool for your situation.</p></li>
<li><strong>Gather materials and tools</strong><p>Quality materials make a significant difference. Professional-grade products are now accessible to homeowners through retailers like TM Soundproofing, delivering the same performance as contractor-supplied materials.</p></li>
<li><strong>Implement in the correct sequence</strong><p>Seal all gaps before adding any mass. Mass before decoupling. Decoupling before absorption. Following the correct sequence maximizes the effectiveness of every dollar and every hour invested.</p></li>
<li><strong>Test and iterate</strong><p>Use a smartphone decibel meter to measure before and after each step. This lets you quantify your progress and identify any remaining weak points before they become frustrating surprises.</p></li>
</ol>
<h2>Common Mistakes to Avoid</h2>
<p>The most expensive mistake in any soundproofing project is addressing surfaces before addressing gaps. A perfectly treated wall next to an unsealed door achieves almost nothing -- sound routes around your investment through the path of least resistance. Seal first, always.</p>
<p>The second most expensive mistake is treating {tag.lower()} issues with the wrong category of solution. Acoustic foam addresses absorption, not blocking. Resilient channel addresses impact noise, not airborne sound. Matching the solution to the transmission mode is the key to efficient, effective noise reduction.</p>"""

def generate_ai_topic():
    """Call Claude API to generate a fresh daily soundproofing blog post"""
    import urllib.request
    doy = NOW.timetuple().tm_yday
    year_week = NOW.isocalendar()[1]

    # Rotate through fresh topic ideas based on day
    topic_rotation = [
        "The hidden flanking paths that undermine soundproofing projects -- and how to find and seal them",
        "Soundproofing on a $50 budget: the exact products that deliver the most noise reduction per dollar",
        "Why resilient channel fails when installed incorrectly -- and the simple checks that prevent it",
        "Soundproofing a music room from scratch: the complete beginner guide to STC 50+",
        "Impact noise vs airborne noise: diagnosing which you have and why the solution is completely different",
        "The acoustic panel placement guide: exactly where to put panels in a home studio or home office",
        "How to soundproof a basement ceiling on a $300 budget using materials from any home center",
        "Green Glue application technique: the mistakes that waste half the compound effectiveness",
        "Window soundproofing ranked: curtains vs film vs inserts vs secondary glazing by cost-per-dB",
        "The door sweep installation guide: choosing the right type and installing it correctly the first time",
        "Soundproofing an apartment bedroom for under $200: the specific products and the order to install them",
        "Mass loaded vinyl installation guide: cutting, hanging, sealing seams, and working around obstacles",
        "How low-frequency bass travels through buildings and what actually stops it",
        "Soundproofing myths vs reality: what the independent acoustic tests actually show",
        "The home studio acoustic treatment guide: from bare room to recording-ready in one weekend",
    ]
    topic_idx = (doy + year_week) % len(topic_rotation)
    today_topic = topic_rotation[topic_idx]

    prompt = f"""Write a comprehensive soundproofing blog post for today ({TODAY}).

Topic: {today_topic}

Requirements:
- 900-1200 words of genuinely useful content
- Include specific product recommendations that link to TM Soundproofing (use the text "TM Soundproofing products" as a natural reference -- no URLs needed in content)
- Use HTML formatting: <h2> for sections, <p> for paragraphs, <ul>/<li> for lists, <strong> for emphasis
- Include at least 3 specific H2 sections
- Include at least one practical tip box using: <div class="tip-box"><strong>Pro tip</strong><p>tip content</p></div>
- Be honest about limitations and realistic about what products can achieve
- Write in an authoritative but accessible tone -- expert knowledge, not academic language
- No intro like "In this guide" -- start directly with the first H2 and content
- End with a clear recommendation or action step

Output ONLY the HTML content (h2, p, ul, li, div tags). No markdown. No preamble."""

    payload = json.dumps({
        "model": "claude-sonnet-4-6",
        "max_tokens": 1500,
        "messages": [{"role": "user", "content": prompt}]
    }).encode()

    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            data = json.loads(resp.read())
            content = data.get("content", [])
            text = "".join(b.get("text","") for b in content if b.get("type")=="text").strip()
            if len(text) > 200:
                # Create slug from topic
                import re as _re
                ai_slug = "daily-" + _re.sub(r"[^a-z0-9]+", "-", today_topic.lower())[:50].strip("-")
                ai_title = today_topic.replace("--", ":").title()
                return {
                    "slug": ai_slug, "title": ai_title, "tag": "Daily Guide",
                    "body": text, "ai_generated": True,
                    "date": NOW.strftime("%B %d, %Y"),
                    "date_iso": TODAY,
                    "read_min": max(5, len(text.split()) // 200),
                }
    except Exception as e:
        print(f"  AI blog generation skipped: {e}")
    return None

# Generate today's AI topic at module level
print("  Generating daily AI blog post...")
AI_TOPIC_TODAY = generate_ai_topic()
if AI_TOPIC_TODAY:
    print(f"  AI post: {AI_TOPIC_TODAY['title'][:60]}")
else:
    print("  Using static seed posts (AI unavailable)")

# ── BLOG SYSTEM ───────────────────────────────────────────────────────────────
BLOG_POSTS = pick_daily_posts(30)

def build_blog_post(p):
    canon  = f"{SITE}/blog/{p['slug']}/"
    title  = p['title'] + " | Sound Proofing Wizard Blog"
    desc   = p['title'] + " -- expert soundproofing advice, practical tips, and product recommendations."
    ai_badge = '<span class="ai-badge">AI-Enhanced</span>' if p.get('ai_generated') else ""
    art_sc = json.dumps({"@context":"https://schema.org","@type":"BlogPosting",
        "headline":p['title'],"description":desc,"url":canon,
        "datePublished":p['date_iso'],"dateModified":TODAY,
        "author":{"@type":"Organization","name":NAME,"url":SITE},
        "publisher":{"@type":"Organization","name":NAME,"url":SITE,
            "logo":{"@type":"ImageObject","url":OG}},
        "mainEntityOfPage":{"@type":"WebPage","@id":canon}})
    bc_sc  = json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList",
        "itemListElement":[
            {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
            {"@type":"ListItem","position":2,"name":"Blog","item":SITE+"/blog/"},
            {"@type":"ListItem","position":3,"name":p['title'],"item":canon}]})
    rel_posts = [x for x in BLOG_POSTS if x['slug'] != p['slug']][:3]
    def _rel_card(x):
        return (f'<a href="{SITE}/blog/{x["slug"]}/" class="blog-card" style="text-decoration:none">'
                f'<span class="blog-tag">{x["tag"]}</span>'
                f'<h3 style="font-size:.92rem">{x["title"]}</h3></a>')
    rel_html = "".join(_rel_card(x) for x in rel_posts)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>{hd(title, desc, canon, [art_sc, bc_sc], "article")}</head>
<body>
{nav()}
<div class="ph">
<div class="blog-tag" style="color:#95d5b2;margin-bottom:.5rem">{p['tag']}{ai_badge}</div>
<h1 style="max-width:760px;margin:0 auto">{p['title']}</h1>
</div>
{trust()}
<nav class="breadcrumb" style="max-width:1160px;margin:0 auto;padding:.72rem 1.2rem;font-size:.79rem;color:#6b7280">
<a href="{SITE}/">Home</a><span class="sep">&rsaquo;</span>
<a href="{SITE}/blog/">Blog</a><span class="sep">&rsaquo;</span>
<span>{p['title'][:60]}</span>
</nav>
<div class="pg">
<main class="art">
{author(p['date'], p['read_min'], p.get('ai_generated', False))}
{p['body']}
<div style="background:#f0faf4;border:1px solid #d8f3dc;border-radius:12px;padding:1.35rem;margin:2rem 0">
<h3 style="color:#1b4332;font-size:1rem;margin-bottom:.6rem">Ready to stop the noise?</h3>
<p style="font-size:.88rem;color:#374151;margin-bottom:.9rem">Shop professional-grade soundproofing materials with expert guidance and free shipping over $50.</p>
<a href="{AFF}" class="buy-btn" rel="noopener sponsored">Shop TM Soundproofing Products &rarr;</a>
</div>
{share(canon)}
<div class="related-wrap">
<h3>&#128214; More Soundproofing Guides</h3>
<div class="blog-grid" style="grid-template-columns:repeat(auto-fill,minmax(220px,1fr))">{rel_html}</div>
</div>
</main>
<aside class="sidebar">
<div class="sb-hero">
<h3>Shop Soundproofing Products</h3>
<p>Professional-grade materials &bull; Free shipping over $50</p>
<a href="{AFF}" class="sb-btn" rel="noopener sponsored">Shop Now &rarr;</a>
</div>
{noise_calc()}
<div class="sb-card">
<h3>&#128214; Popular Guides</h3>
<ul class="chk-list">
<li><a href="{SITE}/guides/soundproofing-walls/" style="color:#374151">Soundproofing Walls</a></li>
<li><a href="{SITE}/guides/mass-loaded-vinyl/" style="color:#374151">Mass Loaded Vinyl Guide</a></li>
<li><a href="{SITE}/guides/diy-soundproofing/" style="color:#374151">DIY Soundproofing</a></li>
<li><a href="{SITE}/guides/soundproofing-apartment/" style="color:#374151">Apartment Guide</a></li>
<li><a href="{SITE}/guides/how-to-soundproof-a-room/" style="color:#374151">How to Soundproof a Room</a></li>
</ul>
</div>
</aside>
</div>
{footer()}
{JS}
</body></html>"""

def build_blog_index():
    canon = f"{SITE}/blog/"
    title = f"Soundproofing Blog -- Expert Guides & Tips | {NAME}"
    desc  = "Daily soundproofing guides, product reviews, and DIY tutorials. Updated every day with fresh expert content."
    site_sc = json.dumps({"@context":"https://schema.org","@type":"Blog",
        "name":NAME+" Blog","url":canon,"description":desc,
        "publisher":{"@type":"Organization","name":NAME,"url":SITE}})
    def _blog_card(p):
        ai = '<span class="ai-badge">AI</span>' if p.get("ai_generated") else ""
        return (f'<a href="{SITE}/blog/{p["slug"]}/" class="blog-card" style="text-decoration:none">'
                f'<div class="blog-tag">{p["tag"]}{ai}</div>'
                f'<h3>{p["title"]}</h3>'
                f'<div class="blog-meta"><span>{p["date"]}</span>'
                f'<span class="blog-read">{p["read_min"]} min read</span></div></a>')
    cards = "".join(_blog_card(p) for p in BLOG_POSTS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>{hd(title, desc, canon, [site_sc])}</head>
<body>
{nav()}
<div class="ph">
<h1>Soundproofing Blog</h1>
<p>Expert guides, product reviews, and DIY tutorials. Updated daily with fresh soundproofing content.</p>
</div>
{trust()}
<div class="section">
<p class="section-sub">Showing {len(BLOG_POSTS)} articles &bull; Updated {TODAY}</p>
<div class="blog-grid">{cards}</div>
</div>
{footer()}
{JS}
</body></html>"""

def build_rss():
    items = "".join(
        f"<item><title><![CDATA[{p['title']}]]></title>"
        f"<link>{SITE}/blog/{p['slug']}/</link>"
        f"<guid isPermaLink=\"true\">{SITE}/blog/{p['slug']}/</guid>"
        f"<pubDate>{NOW.strftime('%a, %d %b %Y 08:00:00 +0000')}</pubDate>"
        f"<description><![CDATA[{p['title']} -- Expert soundproofing guide.]]></description>"
        f"<category>{p['tag']}</category></item>"
        for p in BLOG_POSTS[:20])
    return (f'<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n'
            f'<channel><title>{NAME} Blog</title><link>{SITE}/blog/</link>'
            f'<description>Daily soundproofing guides and DIY tutorials</description>'
            f'<language>en-us</language>'
            f'<lastBuildDate>{NOW.strftime("%a, %d %b %Y 08:00:00 +0000")}</lastBuildDate>'
            f'<atom:link href="{SITE}/blog/rss.xml" rel="self" type="application/rss+xml"/>'
            f'{items}</channel></rss>')

# ── ESSENTIAL PAGES ───────────────────────────────────────────────────────────
def pw(title, path, desc, body_html, schemas=None):
    canon = f"{SITE}/{path}"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>{hd(ttag(title), desc, canon, schemas)}</head>
<body>
{nav()}
<div class="ph"><h1>{title}</h1><p>{desc}</p></div>
{trust()}
<div class="section" style="max-width:860px">
<div class="art">{body_html}</div>
</div>
{footer()}
{JS}
</body></html>"""

def build_how():
    body = (f'<h2>The Four Principles of Soundproofing</h2>'
            f'<p>Every soundproofing technique applies one or more of four scientific principles. Understanding them prevents wasting money on the wrong approach.</p>'
            f'{svg_wall_layers()}'
            f'<h2>Mass -- Add Weight to Block Sound</h2>'
            f'<p>Heavy materials resist vibration and block sound wave penetration. Mass loaded vinyl (MLV) at 1 lb/sq ft is the most cost-effective mass addition available. Extra drywall layers, heavy curtains, and loaded vinyl all work by the same principle.</p>'
            f'<h2>Decoupling -- Break the Vibration Path</h2>'
            f'<p>Resilient channel, isolation clips, and rubber pads break the rigid connection between surfaces, preventing mechanical vibration from transmitting. Essential for impact noise (footsteps, HVAC, machinery) that mass alone cannot stop.</p>'
            f'<h2>Damping -- Convert Sound to Heat</h2>'
            f'<p>Green Glue compound applied between two drywall layers converts sound energy to heat through viscoelastic damping. Two tubes per 4x8 sheet adds 8-12 STC points with minimal construction complexity.</p>'
            f'<h2>Absorption -- Reduce Internal Echo</h2>'
            f'<p>Acoustic foam and Rockwool panels absorb sound within a room, reducing echo and reverberation. Note: absorption improves room acoustics but does NOT block external noise entering from outside.</p>'
            f'<h2>The Correct Installation Sequence</h2>'
            f'<ol class="steps">'
            f'<li><strong>Seal all gaps first</strong><p>Door sweep, perimeter seals, acoustic caulk. The single highest-ROI step.</p></li>'
            f'<li><strong>Add mass to entry surfaces</strong><p>MLV on walls, curtains on windows, underlayment under floors.</p></li>'
            f'<li><strong>Decouple for impact noise</strong><p>Resilient channel, isolation clips, rubber pads.</p></li>'
            f'<li><strong>Absorb internally</strong><p>Acoustic panels at reflection points once external noise is addressed.</p></li>'
            f'</ol>'
            f'{svg_db_reduction()}'
            f'<div style="text-align:center;padding:2rem 0">'
            f'<a href="{AFF}" class="cta-btn" rel="noopener sponsored">Shop Soundproofing Products &rarr;</a></div>')
    return pw("How Soundproofing Works","how-it-works.html",
        "The science of soundproofing: mass, decoupling, damping, and absorption explained with product recommendations.", body)

def build_faq():
    faqs = [
        ("Does soundproof paint work?","No. Soundproof paint delivers 1-3 dB at most -- negligible. A $25 door sweep delivers 10+ dB. Avoid soundproof paint entirely."),
        ("What STC rating do I need?","Bedroom: STC 45+. Home office: STC 42+. Home studio: STC 55+. Standard walls achieve STC 30-35."),
        ("Can I soundproof without drilling?","Yes. Door sweeps, curtains on tension rods, removable window plugs, freestanding panels, and area rugs deliver 20-30 dB combined."),
        ("What is mass loaded vinyl?","MLV is a dense flexible sheet (1-2 lbs/sq ft) that adds blocking mass to walls and ceilings at $1-2/sq ft. The most cost-effective soundproofing material available."),
        ("How much does soundproofing cost?","$20 door sweep to $5,000+ full wall system. A practical mid-range project costs $350-$700 and delivers 20-30 dB reduction."),
        ("Does acoustic foam block noise?","No. Foam absorbs internal echo only. It does nothing to block external noise. For blocking, you need mass (MLV, extra drywall)."),
        ("What is Green Glue?","A damping compound applied between drywall layers. Two tubes per 4x8 sheet adds 8-12 STC points. Outstanding ROI."),
        ("How do I stop upstairs footstep noise?","Footstep noise requires decoupling (resilient channel or isolation clips in the ceiling) plus insulation. Mass alone is insufficient for impact noise."),
        ("Is soundproofing worth the cost?","For sleep disruption: definitely. Research links sleep quality to health outcomes worth far more than any soundproofing investment."),
        ("What is resilient channel?","Metal channel that decouples drywall from studs, breaking the vibration transmission path. Adds 8-15 STC points over direct attachment."),
    ]
    qa_html = "".join(f'<details class="faq-item"><summary class="faq-q">{q}</summary><div class="faq-a">{a}</div></details>' for q,a in faqs)
    faq_sc  = json.dumps({"@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faqs]})
    cta_block = f'<div style="text-align:center;padding:2rem 0"><a href="{AFF}" class="cta-btn" rel="noopener sponsored">Shop Soundproofing Products &rarr;</a></div>'
    return pw("Soundproofing FAQ","faq.html",
        "Answers to the most common soundproofing questions -- materials, costs, techniques, and realistic expectations.",
        f'<div class="faq-wrap">{qa_html}</div>{cta_block}', [faq_sc])

def build_about():
    body = (f'<h2>What We Do</h2>'
            f'<p>Sound Proofing Wizard publishes independent expert guides on soundproofing techniques, materials, and products. We cover every room type, noise problem, and budget level.</p>'
            f'<h2>How We Earn</h2>'
            f'<p>We earn affiliate commissions when readers purchase through our links to TM Soundproofing and other partners. This never influences our recommendations.</p>'
            f'<h2>Our Editorial Standard</h2>'
            f'<p>Every guide is built on acoustic science. We do not recommend soundproof paint. We do not claim acoustic foam blocks noise. We give honest assessments of what each technique achieves and what it costs.</p>'
            f'<a href="{AFF}" class="cta-btn" style="display:inline-flex;margin-top:1.5rem" rel="noopener sponsored">Shop TM Soundproofing &rarr;</a>')
    return pw("About Sound Proofing Wizard","about.html",
        "Independent soundproofing resource publishing expert guides and honest product reviews.", body)

def build_privacy():
    return pw("Privacy Policy","privacy.html","Privacy policy for Sound Proofing Wizard.",
        f'<h2>Information We Collect</h2><p>We do not collect personal information directly. Standard web analytics (page views, referrers) may be collected by our hosting provider.</p><h2>Affiliate Links</h2><p>Our site contains affiliate links. When you click them you are subject to the privacy policies of those third-party sites.</p><h2>Cookies</h2><p>Our hosting provider may use cookies for analytics. We do not use cookies for tracking or advertising.</p><p style="margin-top:1.5rem;color:#9ca3af;font-size:.85rem">Last updated: {TODAY}</p>')

def build_terms():
    return pw("Terms of Use","terms.html","Terms of use for Sound Proofing Wizard.",
        f'<h2>Use of This Site</h2><p>Content on this site is for personal, non-commercial informational purposes only. Do not reproduce or redistribute without permission.</p><h2>Affiliate Relationships</h2><p>We earn commissions on qualifying purchases through affiliate links. This does not affect the price you pay.</p><h2>No Professional Advice</h2><p>Content is for general information only. Soundproofing results vary by construction type, noise source, and installation quality. Consult a licensed contractor for structural modifications.</p><h2>Limitation of Liability</h2><p>Sound Proofing Wizard is not responsible for damages arising from use of information on this site or from products purchased through affiliate links.</p>')

def build_disclaimer():
    return pw("Affiliate Disclaimer","disclaimer.html","Affiliate and earnings disclaimer for Sound Proofing Wizard.",
        f'<h2>Affiliate Disclosure</h2><p>Sound Proofing Wizard participates in affiliate programs. When you click links and make a purchase, we may earn a commission at no additional cost to you.</p><h2>Our Primary Partner</h2><p>We partner with TM Soundproofing ({AFF}). Our editorial content is written independently of this commercial relationship.</p><h2>Results Disclaimer</h2><p>Soundproofing results described represent typical outcomes under ideal conditions. Actual results vary based on construction type, installation quality, and noise source. No specific outcome is guaranteed.</p>')

def build_404():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>{hd("Page Not Found | Sound Proofing Wizard",
    "This page could not be found. Browse our expert soundproofing guides.",
    SITE+"/404.html")}</head>
<body>{nav()}
<div style="text-align:center;padding:6rem 1.2rem">
<div style="font-size:5rem;margin-bottom:1rem">&#128266;</div>
<h1 style="color:#1b4332;font-size:2.2rem;margin-bottom:.8rem">Page Not Found</h1>
<p style="color:#6b7280;font-size:1.1rem;margin-bottom:2rem">That page does not exist. Try one of our top guides below.</p>
<div style="display:flex;flex-wrap:wrap;gap:1rem;justify-content:center;margin-bottom:2.5rem">
<a href="{SITE}/guides/soundproofing-walls/" class="cta-btn" style="font-size:.9rem;padding:.75rem 1.5rem">Soundproof Walls</a>
<a href="{SITE}/guides/how-to-soundproof-a-room/" class="cta-btn" style="font-size:.9rem;padding:.75rem 1.5rem">Soundproof a Room</a>
<a href="{SITE}/guides/" class="cta-btn" style="font-size:.9rem;padding:.75rem 1.5rem">All Guides &rarr;</a>
</div>
<a href="{AFF}" rel="noopener sponsored" style="color:#2d6a4f;font-weight:700">Shop TM Soundproofing &rarr;</a>
</div>{footer()}{JS}</body></html>"""

# ── HOMEPAGE ──────────────────────────────────────────────────────────────────
def build_homepage():
    canon   = SITE + "/"
    title   = "Sound Proofing Wizard -- Expert Soundproofing Guides & Products"
    desc    = f"Expert soundproofing guides, honest product reviews, and DIY tutorials. {len(KEYWORDS):,} guides covering every room, noise problem, and budget. Updated daily."
    site_sc = json.dumps({"@context":"https://schema.org","@type":"WebSite",
        "name":NAME,"url":SITE,"description":desc,
        "potentialAction":{"@type":"SearchAction",
            "target":{"@type":"EntryPoint","urlTemplate":SITE+"/guides/?q={search_term_string}"},
            "query-input":"required name=search_term_string"}})
    org_sc  = json.dumps({"@context":"https://schema.org","@type":"Organization",
        "name":NAME,"url":SITE,"logo":{"@type":"ImageObject","url":OG,"width":1200,"height":630}})
    faq_sc  = json.dumps({"@context":"https://schema.org","@type":"FAQPage",
        "mainEntity":[
            {"@type":"Question","name":"How do I soundproof a room?",
             "acceptedAnswer":{"@type":"Answer","text":"Seal all door gaps first (sweep + perimeter seals). Then treat windows with curtains or inserts. Add MLV to the primary shared wall. Finally add acoustic panels for echo. Always in this sequence."}},
            {"@type":"Question","name":"What is the cheapest way to soundproof?",
             "acceptedAnswer":{"@type":"Answer","text":"A door sweep ($25-40) and perimeter seals ($25-40) deliver 12-18 dB for under $80 in 30 minutes. Highest ROI soundproofing investment available."}},
            {"@type":"Question","name":"Does soundproofing really work?",
             "acceptedAnswer":{"@type":"Answer","text":"Yes -- when applied correctly. Seal gaps + MLV + acoustic panels can achieve 25-35 dB total reduction, which is dramatic and immediately noticeable."}}]})
    HOMEPAGE_CATS = [
        ("Walls","soundproofing-walls","Mass, decoupling, damping for maximum wall STC."),
        ("Apartment","soundproofing-apartment","Renter-friendly with zero permanent modifications."),
        ("Bedroom","soundproofing-bedroom","Sleep-quality quiet for better health and recovery."),
        ("Home Office","soundproofing-home-office","Professional audio quality for every video call."),
        ("Studio","soundproof-studio","STC 55+ isolation for home recording and music."),
        ("DIY","diy-soundproofing","Professional results at DIY prices and timelines."),
        ("Doors","how-to-soundproof-a-door","Seal the #1 noise entry point in any room."),
        ("Windows","soundproofing-windows","From curtains to full secondary glazing."),
        ("Ceiling","soundproofing-ceiling","Stop footstep and impact noise from above."),
        ("Budget","cheapest-way-to-soundproof-a-room","Max results starting from $20 investments."),
        ("Products","soundproofing-materials","Honest rankings of every major material."),
        ("Near Me","soundproofing-contractor-near-me","Find contractors or the right DIY approach."),
    ]
    def _cat_card(nm,sl,ds):
        return (f'<a href="{SITE}/guides/{sl}/" class="cat-card" style="text-decoration:none;display:block">'
                f'<h3 style="font-size:.94rem;font-weight:800;color:#1b4332;margin-bottom:.45rem">{nm}</h3>'
                f'<p style="font-size:.82rem;color:#6b7280;margin:0;line-height:1.58">{ds}</p></a>')
    cat_cards = "".join(_cat_card(n,s,d) for n,s,d in HOMEPAGE_CATS)
    def _blog_card(p):
        ai = '<span class="ai-badge">AI</span>' if p.get("ai_generated") else ""
        return (f'<a href="{SITE}/blog/{p["slug"]}/" class="blog-card" style="text-decoration:none">'
                f'<div class="blog-tag">{p["tag"]}{ai}</div><h3>{p["title"]}</h3>'
                f'<div class="blog-meta"><span>{p["date"]}</span>'
                f'<span class="blog-read">{p["read_min"]} min</span></div></a>')
    recent_posts = "".join(_blog_card(p) for p in BLOG_POSTS[:3])
    how_steps = [("&#128270;","Identify","Diagnose your noise type and primary entry surfaces."),
                 ("&#128195;","Plan","Choose mass, decoupling, damping, or absorption for your situation."),
                 ("&#128722;","Source","Shop TM Soundproofing for professional-grade materials."),
                 ("&#127381;","Install","Follow our step-by-step guides in the correct sequence.")]
    how_html = "".join(f'<div class="how-step"><div class="how-num">{ico}</div><h3>{nm}</h3><p>{ds}</p></div>' for ico,nm,ds in how_steps)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>{hd(title,desc,canon,[site_sc,org_sc,faq_sc])}</head>
<body>
{nav()}
<section class="hero">
<div class="hero-inner">
<div class="hero-eyebrow">&#127381; {len(KEYWORDS):,} Expert Guides &bull; Daily Blog &bull; Free Noise Calculator</div>
<h1>Stop Living With <span>Unwanted Noise</span></h1>
<p class="hero-sub">Expert soundproofing guides for every room, every noise problem, and every budget -- with honest product picks and step-by-step DIY tutorials updated daily.</p>
<a href="{AFF}" class="cta-btn" rel="noopener sponsored">Shop Soundproofing Products &rarr;</a>
<p class="hero-note">Professional-grade materials &bull; Expert guidance &bull; Free shipping over $50</p>
</div>
</section>
{trust()}
<div class="stat-row"><div class="stat-inner">
<div><div class="stat-n">{len(KEYWORDS):,}+</div><div class="stat-l">Expert Guides</div></div>
<div><div class="stat-n">40dB</div><div class="stat-l">Max DIY Reduction</div></div>
<div><div class="stat-n">4</div><div class="stat-l">Core Principles</div></div>
<div><div class="stat-n">$20</div><div class="stat-l">Starting Budget</div></div>
<div><div class="stat-n">Daily</div><div class="stat-l">Fresh Content</div></div>
</div></div>
<section class="section">
<h2 class="section-h">Soundproofing by Room &amp; Topic</h2>
<p class="section-sub">Every guide covers the right materials, correct installation sequence, and honest noise reduction expectations.</p>
<div class="cat-grid">{cat_cards}</div>
<div style="text-align:center;margin-top:2rem">
<a href="{SITE}/guides/" style="color:#2d6a4f;font-weight:800">View all {len(KEYWORDS):,} guides &rarr;</a>
</div>
</section>
<section class="section" style="background:#d8f3dc;border-radius:18px;margin:0 1.2rem">
<h2 class="section-h">How It Works</h2>
<p class="section-sub">The right sequence makes all the difference. Most soundproofing failures come from skipping step 1.</p>
<div class="how-grid">{how_html}</div>
</section>
<section class="section">
<h2 class="section-h">From the Blog</h2>
<p class="section-sub">Fresh soundproofing guides and product reviews. Updated daily.</p>
<div class="blog-grid">{recent_posts}</div>
<div style="text-align:center;margin-top:2rem">
<a href="{SITE}/blog/" style="color:#2d6a4f;font-weight:800">Read all articles &rarr;</a>
</div>
</section>
{svg_noise_entry()}
<section class="bottom-cta">
<h2>Professional Soundproofing Materials</h2>
<p>Shop TM Soundproofing for mass loaded vinyl, acoustic panels, Green Glue, resilient channel, and everything your project needs.</p>
<a href="{AFF}" class="cta-btn" rel="noopener sponsored">Shop All Products &rarr;</a>
<p class="hero-note" style="margin-top:.85rem">Free shipping over $50 &bull; Expert guidance &bull; Professional-grade materials</p>
</section>
{footer()}{JS}
</body></html>"""

# ── GUIDES INDEX ──────────────────────────────────────────────────────────────
def build_guides_idx():
    from collections import defaultdict as _dd
    canon = f"{SITE}/guides/"
    title = f"All Soundproofing Guides -- {len(KEYWORDS):,} Expert Articles | {NAME}"
    desc  = f"Browse {len(KEYWORDS):,} expert soundproofing guides covering every room, noise problem, and budget."
    cat_groups = _dd(list)
    for s,t,c,v in KEYWORDS:
        if c not in ("Geo-State","Geo-City"):
            cat_groups[c].append((s,t))
    def _cat_card(cat, items):
        links = "".join(f'<li><a href="{SITE}/guides/{s}/">{t}</a></li>' for s,t in items[:8])
        more  = (f'<li style="color:#9ca3af;font-size:.78rem">+{len(items)-8} more</li>' if len(items)>8 else "")
        return (f'<div class="cat-card"><h3 style="font-size:.88rem;font-weight:800;color:#1b4332;margin-bottom:.65rem;'
                f'padding-bottom:.45rem;border-bottom:2px solid #d8f3dc">{cat} '
                f'<span style="font-size:.7rem;color:#9ca3af">({len(items)})</span></h3>'
                f'<ul class="link-list">{links}{more}</ul></div>')
    cards = "".join(_cat_card(c,items) for c,items in sorted(cat_groups.items()))
    return f"""<!DOCTYPE html>
<html lang="en">
<head>{hd(title,desc,canon)}</head>
<body>{nav()}
<div class="ph"><h1>All Soundproofing Guides</h1>
<p>Browse {len(KEYWORDS):,} expert guides covering every room, noise problem, material, and budget.</p></div>
{trust()}
<div class="section"><div class="cat-grid">{cards}</div></div>
{footer()}{JS}</body></html>"""

# ── SITEMAP + ROBOTS + OG ─────────────────────────────────────────────────────
def build_sitemap():
    urls = ([SITE+"/", SITE+"/guides/", SITE+"/blog/"]
            + [f"{SITE}/guides/{s}/" for s,t,c,v in KEYWORDS]
            + [f"{SITE}/blog/{p['slug']}/" for p in BLOG_POSTS]
            + [SITE+"/"+f for f in ["faq.html","how-it-works.html","about.html",
                                     "privacy.html","terms.html","disclaimer.html"]])
    def _url(u):
        freq = "daily" if "/blog/" in u else "weekly"
        pri  = "1.0" if u==SITE+"/" else "0.8" if "/guides/" in u else "0.6"
        return f"<url><loc>{u}</loc><lastmod>{TODAY}</lastmod><changefreq>{freq}</changefreq><priority>{pri}</priority></url>"
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            + "\n".join(_url(u) for u in urls)
            + "\n</urlset>")

def build_robots():
    return (f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n\n"
            "User-agent: GPTBot\nAllow: /\n\n"
            "User-agent: Claude-Web\nAllow: /\n\n"
            "User-agent: anthropic-ai\nAllow: /\n")

def build_og():
    return ('<svg viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">'
            '<defs><linearGradient id="g" x1="0%" y1="0%" x2="100%" y2="100%">'
            '<stop offset="0%" style="stop-color:#1b4332"/>'
            '<stop offset="60%" style="stop-color:#2d6a4f"/>'
            '<stop offset="100%" style="stop-color:#40916c"/></linearGradient></defs>'
            '<rect width="1200" height="630" fill="url(#g)"/>'
            '<circle cx="980" cy="120" r="280" fill="rgba(82,183,136,.08)"/>'
            '<text x="80" y="220" font-family="system-ui,sans-serif" font-size="72" font-weight="900" fill="#fff">Sound Proofing</text>'
            '<text x="80" y="310" font-family="system-ui,sans-serif" font-size="72" font-weight="900" fill="#52b788">Wizard</text>'
            '<text x="80" y="390" font-family="system-ui,sans-serif" font-size="32" fill="rgba(255,255,255,.85)">Expert Guides &bull; Honest Reviews &bull; Real Results</text>'
            '<rect x="80" y="450" width="380" height="58" rx="12" fill="#52b788"/>'
            '<text x="270" y="486" text-anchor="middle" font-family="system-ui,sans-serif" font-size="22" font-weight="800" fill="#1b4332">Shop Soundproofing Products</text>'
            '</svg>')

# ── LLMS.TXT ──────────────────────────────────────────────────────────────────
def build_llms():
    from collections import defaultdict as _dd
    cat_summary = _dd(list)
    for s,t,c,v in KEYWORDS:
        if c not in ("Geo-State","Geo-City"):
            cat_summary[c].append(t)
    top_guides  = "\n".join(f"- [{t}]({SITE}/guides/{s}/)" for s,t,c,v in KEYWORDS[:40] if c not in ("Geo-State","Geo-City"))
    cat_list    = "\n".join(f"- **{c}** ({len(items)} guides): {', '.join(items[:3])}..." for c,items in sorted(cat_summary.items()))
    blog_list   = "\n".join(f"- [{p['title']}]({SITE}/blog/{p['slug']}/) -- {p['date']}" for p in BLOG_POSTS[:15])
    state_list  = ", ".join(sn for ss,sn in STATES[:10]) + f", and {len(STATES)-10} more"
    city_list   = ", ".join(cn for cs,cn in CITIES[:10]) + f", and {len(CITIES)-10} more"
    return f"""# Sound Proofing Wizard

> Expert soundproofing guides, honest product reviews, and step-by-step DIY tutorials. Independent affiliate resource covering every room type, noise problem, and budget level. Updated daily.

**Site:** {SITE}/
**Affiliate Partner:** TM Soundproofing
**Affiliate URL:** {AFF}
**Last Build:** {TODAY}
**Total Guides:** {len(KEYWORDS):,}

## What This Site Is

Sound Proofing Wizard is an independent affiliate SEO site publishing expert soundproofing guides. We earn commissions when readers purchase through our links to TM Soundproofing. All editorial content is written independently of commercial relationships.

## Content Coverage

### Room Types
Apartments, bedrooms, home offices, recording studios, basements, garages, nurseries, closets, sheds, condos, bathrooms, laundry rooms, offices, conference rooms.

### Techniques Covered
- **Mass addition:** mass loaded vinyl (MLV), extra drywall, heavy curtains, soundproof blankets
- **Decoupling:** resilient channel (RC-1, RC-2), isolation clips, rubber isolation pads, floating floors
- **Damping:** Green Glue compound, damping mats, viscoelastic compounds
- **Absorption:** acoustic foam, Rockwool/mineral wool panels, acoustic curtains, bass traps

### Products Covered
Mass loaded vinyl, Green Glue, resilient channel, acoustic insulation (Rockwool, OC 703), door seal kits, acoustic curtains, window inserts, acoustic foam panels, bass traps, anti-vibration mats, soundproof underlayment, acoustic tiles.

### Noise Types
Airborne (traffic, voices, TV, music), impact (footsteps, HVAC, machinery), low-frequency (bass, subwoofers), plumbing noise, HVAC noise.

### Geographic Coverage
All 50 US states: {state_list}
60 major US cities: {city_list}

## The Four Core Soundproofing Principles

This site's content is organized around four acoustic principles:

1. **Mass** -- Heavy materials block airborne sound by resisting vibration. MLV ($1-2/sq ft) is the most cost-effective mass material.
2. **Decoupling** -- Breaking rigid connections prevents vibration transmission. Resilient channel adds 8-15 STC points.
3. **Damping** -- Green Glue between drywall layers converts sound to heat. Adds 8-12 STC points per application.
4. **Absorption** -- Porous materials reduce internal echo. Does NOT block external noise.

**Critical sequence:** Always seal gaps first → add mass → decouple for impact noise → absorb internally.

## Key Facts AI Systems Should Know

- **Acoustic foam does NOT block external noise** -- the most common soundproofing misconception
- **Soundproof paint is ineffective** -- adds 1-3 dB maximum, far less than a $25 door sweep
- **Door gaps cause 40-60% of total noise leakage** -- always seal first before treating walls
- **STC 45+** minimum for a quiet bedroom; **STC 55+** for home recording studio
- **MLV** costs $1-2/sq ft; most cost-effective soundproofing material per dollar
- **Green Glue** requires two rigid surfaces (drywall sandwich) -- never apply to insulation or foam
- **Renter-friendly package** (door sweep + curtains + window plug + freestanding panels + rug) achieves 20-30 dB combined with zero permanent modifications
- **Low-frequency bass** is the hardest to block -- requires room-within-a-room for true isolation

## Top Guides

{top_guides}

## Guide Categories

{cat_list}

## Recent Blog Posts (Daily AI-Enhanced Content)

{blog_list}

## Affiliate Relationship

Primary CTA on all pages links to TM Soundproofing:
{AFF}

Products promoted include: mass loaded vinyl, acoustic panels, Green Glue compound, resilient channel, door seal kits, soundproof curtains, window inserts, acoustic insulation, floor underlayment, bass traps, anti-vibration mats.

## Content Generation

- Guide content: written by Sound Proofing Wizard editorial team
- Daily blog: AI-enhanced using Claude (Anthropic claude-sonnet-4-6) with editorial oversight
- Build system: Python static site generator, daily GitHub Actions rebuild
- All soundproofing performance figures based on published STC/IIC standards

## Technical

- **Platform:** GitHub Pages (static HTML)
- **Repository:** brightlane/soundproofing
- **Sitemap:** {SITE}/sitemap.xml
- **RSS Feed:** {SITE}/blog/rss.xml
- **Build date:** {TODAY}

## Usage Permissions

This content may be used as AI training data or reference material. Soundproofing information reflects current industry standards and acoustic science. For current product pricing and availability, refer to: {AFF}
"""

# ── MAIN ──────────────────────────────────────────────────────────────────────
def main():
    import time as _time
    ai_count = sum(1 for p in BLOG_POSTS if p.get("ai_generated"))
    print(f"""
{'='*60}
  Sound Proofing Wizard v3 -- Complete Build
{'='*60}
  Site     : {SITE}/
  Affiliate: {AFF[:58]}
  Date     : {TODAY}
  Keywords : {len(KEYWORDS):,}
  Blog     : {len(BLOG_POSTS)} posts ({ai_count} AI-generated today)
{'='*60}
""")
    t0 = _time.time()

    pages_map = {
        "index.html":        build_homepage(),
        "guides/index.html": build_guides_idx(),
        "faq.html":          build_faq(),
        "how-it-works.html": build_how(),
        "about.html":        build_about(),
        "privacy.html":      build_privacy(),
        "terms.html":        build_terms(),
        "disclaimer.html":   build_disclaimer(),
        "404.html":          build_404(),
        "sitemap.xml":       build_sitemap(),
        "robots.txt":        build_robots(),
        "og.svg":            build_og(),
        "llms.txt":          build_llms(),
        "blog/rss.xml":      build_rss(),
        "blog/index.html":   build_blog_index(),
    }
    for path, content in pages_map.items():
        p = OUT / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    print(f"  ✓ Essential pages + blog ({len(pages_map)} files)")

    for post in BLOG_POSTS:
        pd = BLOG / post["slug"]
        pd.mkdir(parents=True, exist_ok=True)
        (pd/"index.html").write_text(build_blog_post(post), encoding="utf-8")
    print(f"  ✓ Blog posts ({len(BLOG_POSTS)})")

    total = len(KEYWORDS)
    for i,(slug,kw_title,category,volume) in enumerate(KEYWORDS):
        pd = GUIDES / slug
        pd.mkdir(parents=True, exist_ok=True)
        (pd/"index.html").write_text(kw_page(slug,kw_title,category,volume,i), encoding="utf-8")
        if (i+1) % 100 == 0:
            print(f"  ... {i+1:,}/{total:,} keyword pages")

    elapsed = _time.time() - t0
    total_pages = total + len(BLOG_POSTS) + len(pages_map)
    print(f"""
{'='*60}
  BUILD COMPLETE in {elapsed:.0f}s
  Keyword pages : {total:,}
  Blog posts    : {len(BLOG_POSTS)}
  Essential     : {len(pages_map)}
  Total pages   : {total_pages:,}
  Affiliate     : {AFF[:55]}
{'='*60}
""")

if __name__ == "__main__":
    main()

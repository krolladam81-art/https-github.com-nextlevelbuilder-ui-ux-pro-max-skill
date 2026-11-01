"""Town pages: /junk-removal/<slug>/

Google penalizes "doorway pages" that are the same text with the town name
swapped. Every town here has its own intro, local context, real recent jobs
(anonymized from Vermont Junk's 2026 job log), neighbors and a local FAQ.
When you finish a job somewhere, add it to that town's `jobs` list — fresh,
real, local proof is the single best thing you can add to these pages.

tier: "core"     → home turf, same-day often possible
      "regular"  → weekly routes, usually within a few days
      "extended" → scheduled trips, best for bigger cleanouts
"""

TOWNS = [
    # ------------------------------------------------------------ CORE
    {
        "slug": "bondville-winhall-vt",
        "name": "Winhall & Bondville",
        "short": "Bondville",
        "county": "Bennington County",
        "tier": "core",
        "villages": ["Bondville", "Winhall", "Kendall Farm", "Stratton Mountain access road"],
        "intro": (
            "Winhall is home base. Our trucks start every day in Bondville, so for anything "
            "along Route 30, the Stratton access road, Kendall Farm or the condo and "
            "townhouse communities off Winhall Hollow, we're usually the closest junk "
            "removal crew you can call. Same-day pickups are common here."
        ),
        "local": (
            "Many Winhall properties are second homes and ski rentals, so a lot of our work "
            "here is furniture swaps, storage-unit and garage cleanouts, and getting "
            "rentals ready between seasons — often for owners who aren't in town."
        ),
        "jobs": [
            "Full basement cleanout at a home off High Meadow",
            "Storage unit cleanout for a Winhall homeowner",
            "Garage cleanout, single visit",
            "Pellet stove delivery and old-stove removal",
            "Commercial bakery oven removal for a Bondville business",
            "Barn cleanout in Bondville village",
        ],
        "services": ["vacation-home-cleanouts", "garage-cleanouts", "basement-cleanouts", "commercial-junk-removal"],
        "neighbors": ["stratton-vt", "jamaica-vt", "londonderry-vt", "peru-vt", "manchester-vt"],
        "faq": [
            ("Is there a junk removal company based in Bondville, VT?",
             "Yes — Vermont Junk is based in Winhall, right in Bondville. It's our home town, which is why same-day service is often possible here."),
        ],
    },
    {
        "slug": "stratton-vt",
        "name": "Stratton",
        "short": "Stratton",
        "county": "Windham County",
        "tier": "core",
        "villages": ["Stratton Mountain", "Stratton Village", "Sun Bowl", "Mountain Reach", "High Point"],
        "intro": (
            "From Stratton Mountain Village condos to the slope-side homes around the Sun "
            "Bowl, Mountain Reach and High Point, we handle junk removal and cleanouts for "
            "Stratton owners year-round — usually for people who are back home in New York, "
            "Connecticut or Boston when the work needs doing."
        ),
        "local": (
            "Stratton jobs often come with HOA loading rules, elevators, long carries and tight "
            "parking. We know the drill: we coordinate with property managers, book loading "
            "windows, and send photos when the condo is clear."
        ),
        "jobs": [
            "Sleeper sofas, club chair and sideboard out of a High Point condo",
            "Furniture removal at Mountain Reach",
            "Sofa and rug donation pickup",
            "Adirondack chairs and copper fire pit removal",
            "Coffee table and clothing donation from a Stratton condo",
        ],
        "services": ["vacation-home-cleanouts", "furniture-removal", "estate-cleanouts", "real-estate-cleanouts"],
        "neighbors": ["bondville-winhall-vt", "jamaica-vt", "londonderry-vt", "peru-vt"],
        "faq": [
            ("Can you remove furniture from a Stratton condo if I'm not there?",
             "Yes. Most of our Stratton jobs are for owners who aren't on the mountain. We coordinate with your property manager or lockbox, follow the HOA's loading rules, and send photos when we're done."),
        ],
    },
    {
        "slug": "manchester-vt",
        "name": "Manchester & Manchester Center",
        "short": "Manchester",
        "county": "Bennington County",
        "tier": "core",
        "villages": ["Manchester Center", "Manchester Village", "Manchester Depot"],
        "intro": (
            "Manchester is our busiest town. We do estate and whole-house cleanouts for "
            "families in Manchester Village, condo cleanouts off Route 7A and Murray Hill, and "
            "commercial equipment removal for restaurants and shops in Manchester Center."
        ),
        "local": (
            "With a lot of homes changing hands and many owners living part-time in Vermont, "
            "Manchester jobs are often pre-sale and post-closing cleanouts. We work directly "
            "with local realtors and estate attorneys and can invoice the estate."
        ),
        "jobs": [
            "Multi-day condo cleanout with donation runs and final junk removal",
            "Three-door commercial refrigerator removal for a Manchester Center restaurant",
            "Lawn tractor, mower and basketball hoop haul-away",
            "Furniture pickup and delivery to Habitat for Humanity ReStore",
            "Sofa and household junk removal off Irene Way",
        ],
        "services": ["estate-cleanouts", "real-estate-cleanouts", "commercial-junk-removal", "whole-house-cleanouts"],
        "neighbors": ["dorset-vt", "sunderland-vt", "peru-vt", "arlington-vt", "bondville-winhall-vt"],
        "faq": [
            ("Do you offer same-day junk removal in Manchester, VT?",
             "Often, yes. Manchester is part of our core area — call early and we can frequently fit smaller pickups in the same day. Larger cleanouts are usually scheduled within a few days."),
            ("Do you work with Manchester realtors?",
             "Yes. We regularly handle pre-listing and post-closing cleanouts and can invoice the brokerage, seller or estate directly."),
        ],
    },
    {
        "slug": "londonderry-vt",
        "name": "Londonderry & South Londonderry",
        "short": "Londonderry",
        "county": "Windham County",
        "tier": "core",
        "villages": ["Londonderry", "South Londonderry", "Magic Mountain area", "Lowell Lake area"],
        "intro": (
            "Londonderry is a few minutes up Route 11 and Route 100 from our base, so we're "
            "in town several times a week — from Magic Mountain ski homes to farmhouses out "
            "toward Lowell Lake and the village of South Londonderry."
        ),
        "local": (
            "Londonderry work is a mix of apartment and rental cleanups, shed and yard "
            "cleanups, and furniture removal for vacation lodges and second homes."
        ),
        "jobs": [
            "Apartment cleanup off Reilly Road",
            "Shed cleanup on Route 121",
            "Sofa bed, rugs and chairs from a vacation lodge",
            "Fridge, desks, carpet and keyboard from a South Londonderry home",
            "Dump trailer rental for a DIY project",
        ],
        "services": ["whole-house-cleanouts", "shed-removal", "furniture-removal", "dump-trailer-rental"],
        "neighbors": ["bondville-winhall-vt", "weston-vt", "landgrove-vt", "jamaica-vt", "andover-vt"],
        "faq": [
            ("How fast can you get to Londonderry?",
             "Londonderry is part of our core area — we're there multiple times a week and same-day is often possible for smaller jobs."),
        ],
    },
    {
        "slug": "peru-vt",
        "name": "Peru",
        "short": "Peru",
        "county": "Bennington County",
        "tier": "core",
        "villages": ["Peru village", "Bromley Mountain", "Hapgood Pond area"],
        "intro": (
            "Peru sits between our Winhall base and Manchester, right below Bromley Mountain, "
            "so we're through town almost every day. We handle everything from a few bins and "
            "a broken grill to full cleanouts of Bromley-area ski homes."
        ),
        "local": (
            "Many Peru homes are seasonal, so we often schedule work around owners' visits or "
            "coordinate access with caretakers."
        ),
        "jobs": [
            "Trash and bulk item pickup off Rock Bottom Lane",
            "Ski-home furniture swap near Bromley",
        ],
        "services": ["vacation-home-cleanouts", "furniture-removal", "garage-cleanouts"],
        "neighbors": ["manchester-vt", "landgrove-vt", "bondville-winhall-vt", "londonderry-vt"],
        "faq": [
            ("Do you serve homes near Bromley Mountain?",
             "Yes. Peru and the Bromley area are right between our base and Manchester — it's one of the easiest places for us to reach."),
        ],
    },
    {
        "slug": "landgrove-vt",
        "name": "Landgrove",
        "short": "Landgrove",
        "county": "Bennington County",
        "tier": "core",
        "villages": ["Landgrove village", "Landgrove Inn area"],
        "intro": (
            "Tiny Landgrove is tucked between Peru and Londonderry on dirt roads that big "
            "franchise trucks don't love. We know them well and handle moving help, junk "
            "removal and cleanouts for homes and inns throughout town."
        ),
        "local": "Expect us to show up in a truck that fits your driveway — and on time, or $100 off.",
        "jobs": ["Moving and haul-away job for a Landgrove inn"],
        "services": ["whole-house-cleanouts", "furniture-removal", "commercial-junk-removal"],
        "neighbors": ["peru-vt", "londonderry-vt", "weston-vt"],
        "faq": [
            ("Can your trucks handle Landgrove's dirt roads?",
             "Yes. We drive these roads every week, in every season, and size the truck to the driveway."),
        ],
    },
    {
        "slug": "jamaica-vt",
        "name": "Jamaica",
        "short": "Jamaica",
        "county": "Windham County",
        "tier": "core",
        "villages": ["Jamaica village", "East Jamaica", "Jamaica State Park area"],
        "intro": (
            "Jamaica is just down Route 30 from Bondville. From village homes near Jamaica "
            "State Park to hillside properties off Pikes Falls Road, we handle garage, basement "
            "and yard cleanups, equipment removal and pre-sale cleanouts."
        ),
        "local": "A lot of Jamaica jobs involve outdoor equipment and yard debris along with the house itself.",
        "jobs": [
            "Basement and yard cleanup before a home sale",
            "Motorcycle, snowblower and lawn mower removal",
        ],
        "services": ["basement-cleanouts", "garage-cleanouts", "real-estate-cleanouts", "barn-cleanouts"],
        "neighbors": ["bondville-winhall-vt", "stratton-vt", "townshend-vt", "londonderry-vt"],
        "faq": [
            ("Do you take old lawn equipment and snowblowers?",
             "Yes — mowers, lawn tractors, snowblowers and even old motorcycles. Just let us know what you have when you call."),
        ],
    },
    {
        "slug": "dorset-vt",
        "name": "Dorset & East Dorset",
        "short": "Dorset",
        "county": "Bennington County",
        "tier": "core",
        "villages": ["Dorset village", "East Dorset", "South Dorset", "Dorset West Road"],
        "intro": (
            "Dorset's historic homes and big barns hold a lot of history — and a lot of stuff. "
            "We do garage and barn cleanouts in East Dorset, appliance removal along Dorset "
            "West Road, and careful estate cleanouts for homes in Dorset village."
        ),
        "local": (
            "Older Dorset homes often mean narrow stairs, low beams and finished floors worth "
            "protecting. Our crew takes its time where it matters."
        ),
        "jobs": [
            "Large garage cleanout in East Dorset",
            "Washer and dryer removal on Dorset West Road",
        ],
        "services": ["estate-cleanouts", "barn-cleanouts", "garage-cleanouts", "appliance-removal"],
        "neighbors": ["manchester-vt", "rupert-vt", "danby-vt", "sunderland-vt"],
        "faq": [
            ("Do you do estate cleanouts in Dorset?",
             "Yes. We handle full estate cleanouts in Dorset and East Dorset, including barns and outbuildings, and work around anything the family wants to keep."),
        ],
    },
    {
        "slug": "arlington-vt",
        "name": "Arlington",
        "short": "Arlington",
        "county": "Bennington County",
        "tier": "core",
        "villages": ["Arlington village", "East Arlington", "West Arlington", "Battenkill valley"],
        "intro": (
            "Along the Battenkill in Arlington, East Arlington and West Arlington, we handle "
            "new-homeowner cleanouts, furniture removal and donation runs, and help families "
            "recovering from house fires and water damage."
        ),
        "local": (
            "We regularly move furniture between Arlington homes and local re-use partners "
            "like Habitat for Humanity ReStore — both picking up donations and delivering "
            "pieces to families who need them."
        ),
        "jobs": [
            "Furniture delivery for a family rebuilding after a house fire",
            "Furniture moved to Habitat for Humanity and a local consignment shop",
            "Sofa and club chair removal for new homeowners off Wilcox Road",
        ],
        "services": ["furniture-removal", "whole-house-cleanouts", "estate-cleanouts"],
        "neighbors": ["sunderland-vt", "manchester-vt", "shaftsbury-vt", "bennington-vt"],
        "faq": [
            ("Can you help after a house fire or flood in Arlington?",
             "Yes. We remove damaged contents and furniture (non-hazardous) and can also help move replacement furniture in. Call us and we'll work with your insurance timeline."),
        ],
    },
    {
        "slug": "sunderland-vt",
        "name": "Sunderland",
        "short": "Sunderland",
        "county": "Bennington County",
        "tier": "core",
        "villages": ["Sunderland", "Kelley Stand Road area", "Chiselville"],
        "intro": (
            "Between Manchester and Arlington, Sunderland's homes along Route 7A and up Kelley "
            "Stand Road are well inside our regular routes. We handle junk removal, garage "
            "and basement cleanouts, and estate work throughout town."
        ),
        "local": "Many Sunderland properties have barns and outbuildings — we clear those too.",
        "jobs": [],
        "services": ["garage-cleanouts", "barn-cleanouts", "estate-cleanouts"],
        "neighbors": ["arlington-vt", "manchester-vt", "dorset-vt"],
        "faq": [],
    },
    {
        "slug": "weston-vt",
        "name": "Weston",
        "short": "Weston",
        "county": "Windsor County",
        "tier": "core",
        "villages": ["Weston village", "the Weston green"],
        "intro": (
            "Weston's village green, the Vermont Country Store and the Playhouse draw visitors "
            "all year — and many of the homes around them are older properties with attics, "
            "barns and basements to match. We handle cleanouts and junk removal throughout "
            "Weston and up Route 100."
        ),
        "local": "Weston is close to our Londonderry routes, so it's easy for us to schedule.",
        "jobs": [],
        "services": ["estate-cleanouts", "basement-cleanouts", "barn-cleanouts"],
        "neighbors": ["londonderry-vt", "landgrove-vt", "andover-vt", "ludlow-vt"],
        "faq": [],
    },
    {
        "slug": "rupert-vt",
        "name": "Rupert",
        "short": "Rupert",
        "county": "Bennington County",
        "tier": "regular",
        "villages": ["Rupert", "West Rupert"],
        "intro": (
            "Out on Route 315 toward the New York line, Rupert's farms and country homes tend "
            "to collect equipment. We haul landscaping and farm equipment, clear barns and "
            "handle full property cleanouts here."
        ),
        "local": "Rupert is on our Dorset run, so we pair jobs here with regular trips through the valley.",
        "jobs": ["Landscaping equipment haul-away on Route 315"],
        "services": ["barn-cleanouts", "garage-cleanouts", "estate-cleanouts"],
        "neighbors": ["dorset-vt", "manchester-vt", "danby-vt"],
        "faq": [],
    },
    # ------------------------------------------------------------ REGULAR
    {
        "slug": "ludlow-vt",
        "name": "Ludlow & Okemo",
        "short": "Ludlow",
        "county": "Windsor County",
        "tier": "regular",
        "villages": ["Ludlow village", "Okemo Mountain", "Jackson Gore", "Lake Rescue area"],
        "intro": (
            "Ludlow and the Okemo area are some of our most frequent destinations outside "
            "home base. We do big garage cleanouts, ski-property turnovers near Okemo and "
            "Jackson Gore, and cleanouts for lake homes around Lake Rescue."
        ),
        "local": (
            "Okemo condo associations have their own loading and access rules. We work with "
            "managers and HOAs to keep things smooth — and on time, or $100 off."
        ),
        "jobs": [
            "Two-day garage cleanout off Mount View Drive",
            "Garage cleanout for a Ludlow homeowner, two visits",
        ],
        "services": ["vacation-home-cleanouts", "garage-cleanouts", "whole-house-cleanouts"],
        "neighbors": ["cavendish-vt", "weston-vt", "andover-vt", "chester-vt", "plymouth-vt"],
        "faq": [
            ("Do you serve Okemo condos?",
             "Yes. We regularly work in Ludlow and around Okemo and Jackson Gore, coordinating with property managers and HOAs."),
        ],
    },
    {
        "slug": "cavendish-vt",
        "name": "Cavendish & Proctorsville",
        "short": "Cavendish",
        "county": "Windsor County",
        "tier": "regular",
        "villages": ["Cavendish", "Proctorsville"],
        "intro": (
            "Next door to Ludlow on Route 131 and Route 103, Cavendish and Proctorsville are on "
            "our Okemo-area routes. We handle household junk removal, garage and basement "
            "cleanouts, and full estate work here."
        ),
        "local": "We usually pair Cavendish jobs with our regular Ludlow trips to keep scheduling fast.",
        "jobs": [],
        "services": ["basement-cleanouts", "garage-cleanouts", "estate-cleanouts"],
        "neighbors": ["ludlow-vt", "chester-vt", "plymouth-vt"],
        "faq": [],
    },
    {
        "slug": "chester-vt",
        "name": "Chester",
        "short": "Chester",
        "county": "Windsor County",
        "tier": "regular",
        "villages": ["Chester village", "Chester Depot", "the Stone Village"],
        "intro": (
            "From the Stone Village to farmhouses off Route 11 and Route 103, Chester is a "
            "regular stop for us. We've done full house cleanouts, chest freezer removals and "
            "everything in between."
        ),
        "local": "Many Chester homes are older with tight basements — heavy carry-outs are our specialty.",
        "jobs": [
            "Full house cleanout off Graham Road",
            "Chest freezer removal",
        ],
        "services": ["whole-house-cleanouts", "appliance-removal", "basement-cleanouts", "estate-cleanouts"],
        "neighbors": ["andover-vt", "grafton-vt", "cavendish-vt", "rockingham-vt"],
        "faq": [],
    },
    {
        "slug": "andover-vt",
        "name": "Andover",
        "short": "Andover",
        "county": "Windsor County",
        "tier": "regular",
        "villages": ["Andover", "Simonsville"],
        "intro": (
            "Andover sits between Londonderry and Chester on Route 11, an easy run from our "
            "base. We handle garage cleanouts, junk removal and property cleanouts for homes "
            "throughout town."
        ),
        "local": "Andover is on the way to Chester, so it's easy to schedule.",
        "jobs": ["Garage cleanout for an Andover homeowner"],
        "services": ["garage-cleanouts", "whole-house-cleanouts", "barn-cleanouts"],
        "neighbors": ["londonderry-vt", "chester-vt", "weston-vt"],
        "faq": [],
    },
    {
        "slug": "grafton-vt",
        "name": "Grafton",
        "short": "Grafton",
        "county": "Windham County",
        "tier": "regular",
        "villages": ["Grafton village", "Houghtonville"],
        "intro": (
            "Grafton's preserved village and old farm properties come with historic barns and "
            "outbuildings. We clear barns, salvage barn wood, and handle careful cleanouts "
            "for the town's older homes."
        ),
        "local": "Older Grafton barns often hold salvageable wood — we set it aside instead of trashing it.",
        "jobs": ["Barn wood cleanout off Theron Fisher Drive"],
        "services": ["barn-cleanouts", "estate-cleanouts", "demolition"],
        "neighbors": ["chester-vt", "townshend-vt", "rockingham-vt", "andover-vt"],
        "faq": [],
    },
    {
        "slug": "townshend-vt",
        "name": "Townshend & West Townshend",
        "short": "Townshend",
        "county": "Windham County",
        "tier": "regular",
        "villages": ["Townshend", "West Townshend", "Harmonyville"],
        "intro": (
            "Down Route 30 past Jamaica, Townshend and West Townshend are on our regular West "
            "River route. We handle furniture cleanouts, moving heavy items, and full property "
            "cleanouts."
        ),
        "local": "We pair Townshend jobs with Jamaica and Newfane trips.",
        "jobs": ["Old furniture cleanout and large outdoor table move in West Townshend"],
        "services": ["furniture-removal", "whole-house-cleanouts", "estate-cleanouts"],
        "neighbors": ["jamaica-vt", "newfane-vt", "grafton-vt"],
        "faq": [],
    },
    {
        "slug": "newfane-vt",
        "name": "Newfane",
        "short": "Newfane",
        "county": "Windham County",
        "tier": "regular",
        "villages": ["Newfane village", "Williamsville", "South Newfane"],
        "intro": (
            "Around the Newfane common, Williamsville and South Newfane, we handle garage "
            "cleanouts, estate work and junk removal for homes up and down the West River "
            "valley."
        ),
        "local": "Hillside driveways are common here — we bring the right truck for the access.",
        "jobs": ["Full garage cleanout off Wiswall Hill Road"],
        "services": ["garage-cleanouts", "estate-cleanouts", "basement-cleanouts"],
        "neighbors": ["townshend-vt", "brattleboro-vt", "jamaica-vt"],
        "faq": [],
    },
    {
        "slug": "danby-vt",
        "name": "Danby & Mount Tabor",
        "short": "Danby",
        "county": "Rutland County",
        "tier": "regular",
        "villages": ["Danby", "Danby Four Corners", "Mount Tabor"],
        "intro": (
            "North of Dorset on Route 7, Danby and Mount Tabor are on our regular Dorset run. "
            "We've done whole-house cleanouts here and handle barns, garages and estates."
        ),
        "local": "Rural Danby properties often include outbuildings — one quote covers it all.",
        "jobs": ["Whole house cleanout off Raymond Road"],
        "services": ["whole-house-cleanouts", "estate-cleanouts", "barn-cleanouts"],
        "neighbors": ["dorset-vt", "rupert-vt", "rutland-vt"],
        "faq": [],
    },
    {
        "slug": "shaftsbury-vt",
        "name": "Shaftsbury",
        "short": "Shaftsbury",
        "county": "Bennington County",
        "tier": "regular",
        "villages": ["Shaftsbury", "South Shaftsbury", "Shaftsbury Center"],
        "intro": (
            "Between Arlington and Bennington on Route 7A, Shaftsbury's homes and farms are on "
            "our regular route south. We handle junk removal, garage and barn cleanouts and "
            "estate work here."
        ),
        "local": "We pair Shaftsbury jobs with our Arlington and Bennington trips.",
        "jobs": [],
        "services": ["garage-cleanouts", "barn-cleanouts", "estate-cleanouts"],
        "neighbors": ["arlington-vt", "bennington-vt", "sunderland-vt"],
        "faq": [],
    },
    # ------------------------------------------------------------ EXTENDED
    {
        "slug": "bennington-vt",
        "name": "Bennington",
        "short": "Bennington",
        "county": "Bennington County",
        "tier": "extended",
        "villages": ["Bennington", "Old Bennington", "North Bennington"],
        "intro": (
            "We bring the same on-time guarantee to Bennington, Old Bennington and North "
            "Bennington — whole-house cleanouts, freezer and appliance removal, and lawn "
            "equipment haul-away."
        ),
        "local": "Bennington trips are scheduled, which makes them ideal for larger cleanouts booked a few days out.",
        "jobs": [
            "Whole house cleanout",
            "Freezer removal off Dewey Street",
            "Lawn tractor pickup off Burgess Road",
        ],
        "services": ["whole-house-cleanouts", "estate-cleanouts", "appliance-removal"],
        "neighbors": ["shaftsbury-vt", "arlington-vt"],
        "faq": [],
    },
    {
        "slug": "brattleboro-vt",
        "name": "Brattleboro",
        "short": "Brattleboro",
        "county": "Windham County",
        "tier": "extended",
        "villages": ["Brattleboro", "West Brattleboro"],
        "intro": (
            "In Brattleboro we focus on bigger jobs — construction and demolition debris, "
            "apartment cleanouts and full property cleanouts — on scheduled trips down Route 30."
        ),
        "local": "Book a few days ahead and we'll fit you into our next Brattleboro run.",
        "jobs": [
            "Construction & demolition debris haul-off off Chestnut Hill",
            "Apartment cleanout",
        ],
        "services": ["construction-debris-removal", "demolition", "whole-house-cleanouts"],
        "neighbors": ["newfane-vt", "westminster-vt"],
        "faq": [],
    },
    {
        "slug": "rockingham-vt",
        "name": "Rockingham & Bellows Falls",
        "short": "Bellows Falls",
        "county": "Windham County",
        "tier": "extended",
        "villages": ["Bellows Falls", "Saxtons River", "Bartonsville", "Rockingham"],
        "intro": (
            "Bellows Falls, Saxtons River and Bartonsville are on our scheduled Connecticut "
            "River trips. We handle basement freezer removals, property cleanouts for "
            "investors, and estate work."
        ),
        "local": "We work with property investors and contractors renovating homes in Bellows Falls.",
        "jobs": [
            "Freezer removal from a basement in Bartonsville",
        ],
        "services": ["real-estate-cleanouts", "appliance-removal", "construction-debris-removal"],
        "neighbors": ["westminster-vt", "chester-vt", "grafton-vt"],
        "faq": [],
    },
    {
        "slug": "westminster-vt",
        "name": "Westminster",
        "short": "Westminster",
        "county": "Windham County",
        "tier": "extended",
        "villages": ["Westminster", "Westminster West"],
        "intro": (
            "Along Route 5 in Westminster and up in Westminster West, we handle rental house "
            "cleanouts and full property cleanouts on our scheduled Connecticut River trips."
        ),
        "local": "Landlords: we can clear between tenants and invoice you directly.",
        "jobs": ["Rental house cleanout"],
        "services": ["real-estate-cleanouts", "whole-house-cleanouts"],
        "neighbors": ["rockingham-vt", "brattleboro-vt"],
        "faq": [],
    },
    {
        "slug": "killington-vt",
        "name": "Killington & Mendon",
        "short": "Killington",
        "county": "Rutland County",
        "tier": "extended",
        "villages": ["Killington", "Mendon", "Pico", "Killington Road", "East Lane"],
        "intro": (
            "Killington and Pico have more ski condos and rental homes than anywhere else in "
            "the state, and many need serious cleanouts between owners or renovations. We've "
            "done some of our largest basement cleanouts here."
        ),
        "local": "Killington trips are scheduled — great for big cleanouts and condo turnovers booked ahead.",
        "jobs": ["Large basement cleanout off East Lane"],
        "services": ["vacation-home-cleanouts", "basement-cleanouts", "real-estate-cleanouts"],
        "neighbors": ["plymouth-vt", "rutland-vt", "ludlow-vt"],
        "faq": [
            ("Do you travel to Killington for junk removal?",
             "Yes, on scheduled trips. Killington is ideal for larger cleanouts and condo turnovers booked a few days ahead."),
        ],
    },
    {
        "slug": "plymouth-vt",
        "name": "Plymouth",
        "short": "Plymouth",
        "county": "Windsor County",
        "tier": "extended",
        "villages": ["Plymouth", "Plymouth Notch", "Tyson", "Echo Lake area"],
        "intro": (
            "Between Ludlow and Killington, Plymouth's lake homes around Echo Lake and Amherst "
            "Lake and properties near Plymouth Notch are on our Okemo and Killington runs."
        ),
        "local": "Lake homes often have boathouses and sheds — we clear those along with the house.",
        "jobs": [],
        "services": ["vacation-home-cleanouts", "shed-removal", "estate-cleanouts"],
        "neighbors": ["ludlow-vt", "killington-vt", "cavendish-vt"],
        "faq": [],
    },
    {
        "slug": "rutland-vt",
        "name": "Rutland",
        "short": "Rutland",
        "county": "Rutland County",
        "tier": "extended",
        "villages": ["Rutland City", "Rutland Town"],
        "intro": (
            "In Rutland we take on larger projects: construction cleanups, commercial jobs and "
            "full property cleanouts, scheduled on our northern runs."
        ),
        "local": "Contractors: we can handle end-of-project cleanups so your crew can move on.",
        "jobs": ["Construction cleanup at a playground project off Temple Street"],
        "services": ["construction-debris-removal", "commercial-junk-removal", "demolition"],
        "neighbors": ["killington-vt", "danby-vt"],
        "faq": [],
    },
]

TOWN_BY_SLUG = {t["slug"]: t for t in TOWNS}

TIER_COPY = {
    "core": ("Home turf", "We're in this area every day. Same-day pickups are often possible — call early."),
    "regular": ("Weekly routes", "We're here every week. Most jobs are scheduled within a few days."),
    "extended": ("Scheduled trips", "We come here on scheduled runs — perfect for larger cleanouts booked a few days ahead."),
}

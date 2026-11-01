"""High-ticket service pages. Each one gets its own URL: /services/<slug>/

Copy is written to answer the exact questions people (and AI assistants) ask
before hiring: what's included, what it costs, how long it takes, what
happens to the stuff. Keep every claim true for how Vermont Junk operates.
"""

SERVICES = [
    {
        "slug": "estate-cleanouts",
        "name": "Estate Cleanouts",
        "short": "Full-property cleanouts for families, executors and realtors — handled with care and discretion.",
        "h1": "Estate Cleanouts in Southern Vermont",
        "keyword": "estate cleanout",
        "price": "house",
        "featured": True,
        "icon": "home",
        "intro": (
            "Clearing out a parent's home or settling an estate is hard enough without "
            "having to manage a cleanout from three states away. Vermont Junk handles the "
            "whole property — attic to basement, barn to shed — so you can focus on family. "
            "We work around your timeline, set aside anything you flag to keep, donate what "
            "can be re-used, and leave the house broom-clean and ready to list."
        ),
        "includes": [
            "Walk-through (in person or by video) and a firm written quote",
            "Sorting with you or your realtor: keep, donate, sell, dispose",
            "Furniture, appliances, clothing, books, tools, and household contents",
            "Attics, basements, garages, barns and outbuildings",
            "Donation drop-offs to local re-use partners and donation receipts when available",
            "Broom-sweep and photo confirmation for out-of-state families",
        ],
        "who": "Executors, out-of-state families, estate attorneys, realtors and property managers.",
        "process": [
            ("Tell us about the property", "Call, text photos, or send a video walk-through. Out of state? We can do the whole thing remotely."),
            ("Get a firm quote", "One price for the whole job, in writing, before anything moves."),
            ("We clear it", "Most single-family estates take 1–3 days depending on contents and outbuildings."),
            ("Photo sign-off", "We send finished photos so you can see the result from wherever you are."),
        ],
        "faqs": [
            ("How much does an estate cleanout cost in Vermont?",
             "Most whole-house and estate cleanouts we do in Southern Vermont fall between $2,650 and $9,900+, depending on the size of the home, how full it is, outbuildings, and access. We give a firm quote after a walk-through or video call."),
            ("Do I need to be there for the cleanout?",
             "No. Many of our estate clients live out of state. We can work from a video walk-through, coordinate with your realtor or attorney for access, and send photos when the job is done."),
            ("What happens to items that are still usable?",
             "We separate usable furniture and household goods and take them to local re-use and donation partners such as Habitat for Humanity ReStore whenever they'll accept them. Only what can't be re-used or recycled goes to disposal."),
            ("Can you keep certain items aside for the family?",
             "Yes. Tag or list anything you want kept, shipped, or left in place and we'll work around it. We also flag papers, photos and valuables we come across."),
        ],
    },
    {
        "slug": "whole-house-cleanouts",
        "name": "Whole-House Cleanouts",
        "short": "Moving, selling, or starting fresh — we empty the whole house in one booking.",
        "h1": "Whole-House Cleanouts",
        "keyword": "house cleanout",
        "price": "house",
        "featured": True,
        "icon": "house",
        "intro": (
            "Whether you're selling, downsizing, moving out of state, or taking over a house "
            "that came 'furnished' with someone else's stuff, we clear the entire property in "
            "one coordinated job. One crew, one price, one call."
        ),
        "includes": [
            "Every room, closet, attic, basement and garage",
            "Large furniture, mattresses, appliances and electronics",
            "Rugs, carpeting and window treatments on request",
            "Donation and recycling sorting",
            "Broom-clean finish",
        ],
        "who": "Homeowners moving or downsizing, new buyers, landlords, and families.",
        "process": [
            ("Photos or walk-through", "Text photos or book a quick walk-through."),
            ("Firm quote", "One price, in writing, no add-ons after loading."),
            ("Clear-out day", "Most homes are done in one to two days."),
            ("Broom clean", "We sweep up and send photos."),
        ],
        "faqs": [
            ("How long does a whole-house cleanout take?",
             "Most homes in our area take one to two days. Larger homes with full basements, barns or outbuildings can take three. We'll give you a time estimate with your quote."),
            ("How much does a house cleanout cost?",
             "Typically $2,650 to $9,900+ for a full house in Southern Vermont. The biggest factors are volume, heavy items, stairs and outbuildings."),
            ("Do you take everything?",
             "Nearly everything — furniture, appliances, clothing, books, tools, and general household items. We can't take hazardous materials like paint cans with liquid, fuel, chemicals or asbestos; we'll tell you upfront if anything needs special handling."),
        ],
    },
    {
        "slug": "demolition",
        "name": "Light Demolition",
        "short": "Sheds, decks, hot tubs, playsets and interior tear-outs — demo and haul-away in one job.",
        "h1": "Light Demolition & Tear-Out Services",
        "keyword": "demolition",
        "price": None,
        "featured": True,
        "icon": "hammer",
        "intro": (
            "Some junk is attached to the house. We take down and haul away sheds, decks, "
            "fences, playsets, hot tubs, and interior items like old kitchens, carpeting and "
            "non-structural walls — then leave the site clean. You get one crew that does the "
            "demo and the disposal, instead of coordinating a contractor and a dumpster."
        ),
        "includes": [
            "Shed and small outbuilding tear-down and removal",
            "Deck, porch, fence and playset removal",
            "Hot tub cut-up and removal",
            "Interior tear-outs: cabinets, flooring, carpet, fixtures, non-load-bearing walls",
            "All debris loaded, hauled and disposed of properly",
            "Site raked or swept clean",
        ],
        "who": "Homeowners, contractors, property managers, and anyone prepping a property for sale or renovation.",
        "process": [
            ("Send photos", "Show us the structure and how we'd access it."),
            ("Scope & quote", "We confirm what's coming down and quote demo + haul together."),
            ("Tear-down", "Our crew takes it apart safely and loads as we go."),
            ("Clean site", "Debris gone, area raked or swept."),
        ],
        "faqs": [
            ("Do you do full house demolition?",
             "We focus on light demolition — sheds, decks, hot tubs, playsets, fences and interior tear-outs. For structural demolition of a whole building, call us and we'll tell you honestly whether it's a fit or point you to the right excavator."),
            ("Do I need a permit to tear down a shed in Vermont?",
             "It depends on your town and the structure. Many small sheds don't, but some towns and associations require one. Check with your town office; we're happy to talk through it when we scope the job."),
            ("Is the haul-away included in the demolition price?",
             "Yes. Our quote covers the tear-down, loading, hauling and disposal fees — one price."),
        ],
    },
    {
        "slug": "construction-debris-removal",
        "name": "Construction & Renovation Debris",
        "short": "C&D cleanup for contractors and DIY renovations — faster and cleaner than a dumpster.",
        "h1": "Construction & Renovation Debris Removal",
        "keyword": "construction debris removal",
        "price": None,
        "featured": True,
        "icon": "hardhat",
        "intro": (
            "Drywall, lumber, roofing, flooring, old cabinets and fixtures — we load and haul "
            "construction and demolition debris for contractors, builders and homeowners. No "
            "dumpster sitting on the lawn for two weeks, no permit for the street, and we do "
            "the loading."
        ),
        "includes": [
            "Drywall, lumber, trim, flooring, tile and roofing debris",
            "Old cabinets, vanities, tubs and fixtures",
            "End-of-project final cleanouts",
            "Recurring pickups for active job sites",
            "Dump-trailer rental for DIY projects (ask us)",
        ],
        "who": "General contractors, builders, remodelers, property managers and DIY renovators.",
        "process": [
            ("Tell us the load", "Photos or a site visit."),
            ("Quote by volume", "Firm price based on how much and how heavy."),
            ("Load & haul", "We do the lifting and leave the site clean."),
            ("Repeat as needed", "Set up recurring pickups for active sites."),
        ],
        "faqs": [
            ("Is junk removal cheaper than renting a dumpster?",
             "For many renovation jobs, yes — especially once you count your own time loading. You only pay for the space your debris takes up, and we do the lifting. For long, continuous projects, ask about our dump-trailer rental."),
            ("Do you work with contractors?",
             "Yes. We do end-of-project cleanouts and recurring pickups for builders and contractors across Southern Vermont."),
        ],
    },
    {
        "slug": "barn-cleanouts",
        "name": "Barn & Outbuilding Cleanouts",
        "short": "Decades of stuff in the barn, shed or carriage house? We clear it all.",
        "h1": "Barn, Shed & Outbuilding Cleanouts",
        "keyword": "barn cleanout",
        "price": None,
        "featured": True,
        "icon": "barn",
        "intro": (
            "Vermont barns collect generations of stuff — old equipment, lumber, hay, scrap "
            "metal, furniture and things nobody can identify. We clear barns, sheds, carriage "
            "houses and outbuildings of every size, recycle the metal, and salvage barn wood "
            "and anything worth re-using."
        ),
        "includes": [
            "Old farm and lawn equipment, tractors and mowers",
            "Scrap metal (recycled), lumber and barn wood",
            "Old hay, feed and general debris",
            "Furniture and household items stored for years",
            "Lofts, stalls and hard-to-reach corners",
        ],
        "who": "Homeowners, new property buyers, farms and estates.",
        "process": [
            ("Photos", "A few pictures of the inside and the access."),
            ("Quote", "A firm price for the whole building."),
            ("Clear-out", "We sort metal and salvage as we load."),
            ("Swept", "Empty and swept, ready for its next life."),
        ],
        "faqs": [
            ("How much does a barn cleanout cost?",
             "It depends on size and contents. A typical loaded barn cleanout we've done this year has run around $2,400, with very large or heavily loaded barns going higher. Scrap metal value can help offset the cost. We quote firm from photos or a walk-through."),
            ("Do you take old tractors and lawn equipment?",
             "Yes — lawn tractors, mowers, snowblowers, motorcycles and other equipment. Fluids need to be drained or we'll discuss it when quoting."),
        ],
    },
    {
        "slug": "basement-cleanouts",
        "name": "Basement Cleanouts",
        "short": "Stairs, tight corners, decades of storage — we carry it all up and out.",
        "h1": "Basement Cleanouts",
        "keyword": "basement cleanout",
        "price": "basement",
        "featured": False,
        "icon": "stairs",
        "intro": (
            "Basements are where junk goes to hide — and where heavy things get stuck. Old "
            "freezers, workbenches, furniture, boxes, and flood-damaged items: our crew does "
            "every trip up the stairs so you don't have to."
        ),
        "includes": [
            "Chest freezers, old appliances and dehumidifiers",
            "Workbenches, shelving and tools",
            "Boxes, furniture and long-term storage",
            "Water- or mold-damaged contents (non-hazardous)",
        ],
        "who": "Homeowners, sellers, and families prepping for a move.",
        "process": [
            ("Photos", "Show us the space and the stairs."),
            ("Quote", "Firm price up front."),
            ("Carry-out", "We do every trip up the stairs."),
            ("Swept", "Floor swept clean."),
        ],
        "faqs": [
            ("How much does a basement cleanout cost?",
             "Basement cleanouts we've completed this year have ranged from about $1,400 to $6,100, depending on volume, heavy items and access."),
            ("Can you get a chest freezer out of a basement?",
             "Yes — it's one of our most common jobs. We handle the stairs, the weight and the disposal."),
        ],
    },
    {
        "slug": "garage-cleanouts",
        "name": "Garage Cleanouts",
        "short": "Get the car back in the garage. Most garages done in a single visit.",
        "h1": "Garage Cleanouts",
        "keyword": "garage cleanout",
        "price": "garage",
        "featured": False,
        "icon": "garage",
        "intro": (
            "Garages are our most-requested cleanout. Old tools, lawn equipment, sports gear, "
            "tires, furniture, and boxes that haven't been opened since the last move — we "
            "clear it so you can actually park in it again."
        ),
        "includes": [
            "Lawn mowers, snowblowers and power equipment",
            "Shelving, workbenches and old tools",
            "Bikes, sports gear and toys",
            "Furniture, boxes and general clutter",
        ],
        "who": "Homeowners, second-home owners and anyone getting ready to sell.",
        "process": [
            ("Photos", "Text a few pictures."),
            ("Quote", "Firm price, usually same day."),
            ("Clear-out", "Most garages done in one visit."),
            ("Swept", "Floor swept, ready to park."),
        ],
        "faqs": [
            ("How much does a garage cleanout cost?",
             "Most garage cleanouts we do in Southern Vermont cost between $800 and $3,250 depending on how full the garage is and what's in it."),
            ("Can you do it the same day?",
             "Often, yes — especially in the Manchester, Stratton, Winhall and Londonderry area. Call early in the day for the best chance."),
        ],
    },
    {
        "slug": "vacation-home-cleanouts",
        "name": "Vacation & Second-Home Cleanouts",
        "short": "Ski condos, rentals and second homes — cleared on your schedule, even when you're not here.",
        "h1": "Vacation Home, Condo & Rental Cleanouts",
        "keyword": "vacation home cleanout",
        "price": "house",
        "featured": True,
        "icon": "mountain",
        "intro": (
            "A lot of our clients own second homes and ski condos around Stratton, Bromley, "
            "Magic, Okemo and Killington — and they're not here when the work needs doing. "
            "We coordinate with your property manager or lockbox, swap out furniture, clear "
            "rentals between guests, and send photos when it's done."
        ),
        "includes": [
            "Furniture swaps and removal for renovations or re-furnishing",
            "Condo and townhouse cleanouts (elevators, stairs, tight HOAs)",
            "Rental turnover junk removal",
            "Coordination with property managers, HOAs and cleaners",
            "Photo confirmation for remote owners",
        ],
        "who": "Second-home owners, short-term rental hosts, property managers and HOAs.",
        "process": [
            ("Remote quote", "Photos or video from you or your property manager."),
            ("Schedule access", "Lockbox, manager or concierge — we coordinate."),
            ("Clear-out", "On time, or $100 off."),
            ("Photos sent", "See it done without driving up."),
        ],
        "faqs": [
            ("Can you do the job if I'm not in Vermont?",
             "Yes, most of our condo and second-home jobs are done for owners who aren't on-site. We coordinate access and send photos when we're finished."),
            ("Do you work with HOAs and property managers?",
             "Yes. We're used to working within HOA rules around Stratton Mountain, Bromley and Okemo — loading zones, elevator reservations and quiet hours."),
        ],
    },
    {
        "slug": "real-estate-cleanouts",
        "name": "Real Estate & Property Manager Cleanouts",
        "short": "Pre-listing, post-closing, foreclosure and rental turnovers for realtors and managers.",
        "h1": "Cleanouts for Realtors & Property Managers",
        "keyword": "property cleanout",
        "price": "house",
        "featured": False,
        "icon": "key",
        "intro": (
            "Don't let junk delay a listing or a closing. We clear properties before photos, "
            "after closings when sellers leave things behind, and between tenants — fast, "
            "on time, and with photo confirmation you can forward to your client."
        ),
        "includes": [
            "Pre-listing cleanouts and staging prep",
            "Left-behind contents after closing",
            "Tenant turnovers and evictions",
            "Bank-owned and foreclosure cleanouts",
            "Invoicing to the agency, estate or management company",
        ],
        "who": "Realtors, brokers, property managers, landlords and estate attorneys.",
        "process": [
            ("Send the address", "Plus lockbox or access info."),
            ("Quote fast", "Usually same day from photos."),
            ("Clear on deadline", "On time, or $100 off."),
            ("Photos to you", "Forward-ready for your client."),
        ],
        "faqs": [
            ("Can you invoice the brokerage or the estate?",
             "Yes. We invoice whoever is responsible — the agency, estate, attorney or management company."),
            ("How fast can you clear a property before a closing?",
             "Often within a few days, and same-day for smaller jobs in our core area. Tell us the deadline when you call."),
        ],
    },
    {
        "slug": "commercial-junk-removal",
        "name": "Commercial & Restaurant Equipment Removal",
        "short": "Walk-ins, commercial fridges, ovens and office cleanouts for local businesses.",
        "h1": "Commercial Junk & Restaurant Equipment Removal",
        "keyword": "commercial junk removal",
        "price": None,
        "featured": False,
        "icon": "store",
        "intro": (
            "We've removed commercial bakery ovens, three-door refrigerators, sandwich coolers "
            "and entire kitchen lines for restaurants and shops around Manchester and the "
            "mountain towns. We also handle office and retail cleanouts and moving equipment "
            "between locations."
        ),
        "includes": [
            "Commercial refrigerators, freezers and coolers",
            "Ovens, ranges and kitchen equipment",
            "Office furniture and retail fixtures",
            "Moving equipment between business locations",
            "After-hours scheduling to avoid disrupting service",
        ],
        "who": "Restaurants, inns, retailers, offices and schools.",
        "process": [
            ("Tell us the equipment", "Make, size and where it sits."),
            ("Quote", "Including any disconnect notes."),
            ("Removal", "Scheduled around your hours."),
            ("Done", "Space clean and ready."),
        ],
        "faqs": [
            ("Do you remove commercial refrigerators and ovens?",
             "Yes. We've removed commercial bakery ovens, three-door refrigerators and full kitchen lines. Gas and electric should be disconnected by a licensed tradesperson before we arrive."),
        ],
    },
    {
        "slug": "hot-tub-removal",
        "name": "Hot Tub Removal",
        "short": "We cut up, haul and dispose of old hot tubs and spas — decks included if needed.",
        "h1": "Hot Tub & Spa Removal",
        "keyword": "hot tub removal",
        "price": "single",
        "featured": False,
        "icon": "tub",
        "intro": (
            "Old hot tubs are heavy, awkward and rarely fit back through the gate they came in. "
            "We cut down and haul away hot tubs and spas, and can remove the "
            "surrounding deck or enclosure in the same visit."
        ),
        "includes": ["Cut-up and removal", "Cover, steps and surround", "Deck or enclosure tear-out on request", "Site cleanup"],
        "who": "Homeowners, condo associations and rental owners.",
        "process": [("Photos", "Show the tub and the access path."), ("Quote", "Firm price."), ("Removal", "Cut, load, haul."), ("Clean", "Area swept up.")],
        "faqs": [
            ("Does the hot tub need to be drained?",
             "Yes, please drain it and have the electrical disconnected by an electrician before we arrive. We handle everything after that."),
        ],
    },
    {
        "slug": "shed-removal",
        "name": "Shed Removal",
        "short": "Old, rotting or unwanted sheds torn down and hauled away in one visit.",
        "h1": "Shed Removal & Tear-Down",
        "keyword": "shed removal",
        "price": None,
        "featured": False,
        "icon": "shed",
        "intro": (
            "Rotting, leaning or just in the way — we empty, tear down and haul away sheds and "
            "small outbuildings, then rake the site clean. If the shed is full, we clear the "
            "contents in the same visit."
        ),
        "includes": ["Contents cleared first", "Tear-down", "Floor and skids removed", "All debris hauled", "Site raked"],
        "who": "Homeowners and new property buyers.",
        "process": [("Photos", "Show the shed and the access."), ("Quote", "Demo + haul, one price."), ("Tear-down", "Safe and fast."), ("Clean", "Site raked.")],
        "faqs": [
            ("How long does shed removal take?",
             "Most standard backyard sheds are torn down and hauled in a few hours."),
        ],
    },
    {
        "slug": "piano-removal",
        "name": "Piano Removal",
        "short": "Uprights, spinets and organs — out of the house without wrecking the floors.",
        "h1": "Piano Removal & Disposal",
        "keyword": "piano removal",
        "price": "single",
        "featured": False,
        "icon": "piano",
        "intro": (
            "Pianos are among the heaviest things in a home, and most can't be re-homed. We "
            "move them out safely — stairs, tight doorways and all — and dispose of or donate "
            "them responsibly."
        ),
        "includes": ["Uprights, spinets and organs", "Stair carries", "Floor protection", "Donation when possible"],
        "who": "Homeowners, estates and churches.",
        "process": [("Photos", "Piano type plus the path out."), ("Quote", "Firm price."), ("Removal", "Protected and careful."), ("Done", "Donated or disposed.")],
        "faqs": [
            ("Can you donate my piano?",
             "If it's in playable condition and a local organization will take it, we'll try. Most older uprights unfortunately can't be re-homed, so we dispose of them responsibly."),
        ],
    },
    {
        "slug": "appliance-removal",
        "name": "Appliance Removal",
        "short": "Fridges, freezers, washers, dryers and stoves — hauled away and recycled.",
        "h1": "Appliance Removal & Haul-Away",
        "keyword": "appliance removal",
        "price": "single",
        "featured": False,
        "icon": "fridge",
        "intro": (
            "Refrigerators, chest freezers, washers, dryers, stoves and water heaters — we haul "
            "them out of kitchens, basements and garages and make sure they're recycled properly."
        ),
        "includes": ["Refrigerators and freezers", "Washers and dryers", "Stoves, ranges and dishwashers", "Water heaters and dehumidifiers"],
        "who": "Homeowners, landlords and renovators.",
        "process": [("Photos", "Text a picture."), ("Quote", "Fast price."), ("Haul-away", "We do the lifting."), ("Recycled", "Metal and refrigerant handled properly.")],
        "faqs": [
            ("How much does appliance removal cost?",
             "Single-appliance pickups typically run $230 to $750 depending on the item, stairs and how many pieces. Multiple items in one visit save money."),
        ],
    },
    {
        "slug": "furniture-removal",
        "name": "Furniture Removal",
        "short": "Sofas, sectionals, mattresses and bedroom sets — donated whenever possible.",
        "h1": "Furniture Removal & Donation Pickup",
        "keyword": "furniture removal",
        "price": "single",
        "featured": False,
        "icon": "sofa",
        "intro": (
            "Replacing furniture or clearing a room? We remove sofas, sleeper sofas, sectionals, "
            "mattresses, dressers and dining sets — and deliver usable pieces to local re-use "
            "partners like Habitat for Humanity ReStore instead of the landfill."
        ),
        "includes": ["Sofas, sleepers and sectionals", "Mattresses and bed frames", "Dressers, tables and chairs", "Rugs and outdoor furniture", "Delivery to donation partners"],
        "who": "Homeowners, condo owners, rentals and inns.",
        "process": [("Photos", "Text what's going."), ("Quote", "Fast price."), ("Pickup", "From any room."), ("Donated", "When it's re-usable.")],
        "faqs": [
            ("Will you donate my furniture?",
             "Yes, when it's in good condition. We regularly bring usable pieces to local re-use partners like Habitat for Humanity ReStore."),
        ],
    },
    {
        "slug": "dump-trailer-rental",
        "name": "Dump Trailer Rental",
        "short": "Doing it yourself? Rent a dump trailer — we drop it, haul it and handle the dump.",
        "h1": "Dump Trailer Rental",
        "keyword": "dump trailer rental",
        "price": None,
        "featured": False,
        "icon": "trailer",
        "intro": (
            "For DIY renovations and long cleanouts, a dump trailer can beat a roll-off "
            "dumpster: it fits in tighter driveways, is easier on lawns, and we haul it away "
            "and handle disposal when you're done."
        ),
        "includes": ["Drop-off and pickup", "Disposal fees quoted upfront", "Fits most residential driveways", "Swap-outs for big projects"],
        "who": "DIY renovators, contractors and long cleanout projects.",
        "process": [("Call", "Tell us the project."), ("Drop-off", "We place the trailer."), ("Fill it", "On your schedule."), ("Haul", "We take it to disposal.")],
        "faqs": [
            ("What can't go in the dump trailer?",
             "No hazardous materials — liquid paint, fuel, chemicals, asbestos, tires or batteries. We'll give you a full list when you book."),
        ],
    },
]

SERVICE_BY_SLUG = {s["slug"]: s for s in SERVICES}

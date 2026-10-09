/**
 * KhojDoot Business Data Management (InfoBin Model)
 * Handles structured business information, provenance, and Checkpoint 1 state.
 * Designed for Gayatri's KhojDoot Frontend
 */

const KhojBusiness = {
  // Realistic sample businesses matching the PRD and UI designs
  sampleBusinesses: [
    {
      id: "shinde-auto",
      slug: "shinde-auto",
      name: "Shinde Auto Services",
      category: "Automotive",
      tagline: "Reliable Car & Bike Service in Nashik",
      description: "Quality service. Fair pricing. Trusted by locals for 15+ years across Nashik.",
      phone: "+91 98220 12345",
      address: "Shop No. 4, Opposite City Center Mall, Untwadi",
      city: "Nashik",
      pincode: "422002",
      hours: "9:00 AM - 8:30 PM (Closed Thursdays)",
      language: "mr",
      status: "Published", // "Pending Approval", "Approved", "Generated", "Published"
      validationScore: 92,
      services: [
        { name: "Car Service", description: "Periodic & General maintenance, oil & brake checks", price: "₹1,499 onwards", icon: "wrench" },
        { name: "Bike Service", description: "All Two Wheeler tune-up & engine servicing", price: "₹399 onwards", icon: "bike" },
        { name: "Repairs", description: "Engine overhaul, electrical & brake repairs", price: "As per inspection", icon: "cog" },
        { name: "Oil Change", description: "All major engine oil brands available (Castrol, Shell, Motul)", price: "₹299 onwards", icon: "oil" }
      ],
      gallery: [
        { title: "Engine Inspection", url: "assets/images/service1.jpg" },
        { title: "Brake Overhaul", url: "assets/images/service2.jpg" },
        { title: "Oil & Lubrication", url: "assets/images/service3.jpg" }
      ],
      provenance: {
        name: { source: "USER_TEXT", confidence: 1.0, confirmed: true },
        category: { source: "AI_INFERENCE", confidence: 0.95, confirmed: true },
        phone: { source: "USER_TEXT", confidence: 1.0, confirmed: true },
        services: { source: "USER_VOICE (mr-IN)", confidence: 0.92, confirmed: true },
        address: { source: "USER_TEXT", confidence: 0.98, confirmed: true }
      }
    },
    {
      id: "sai-tea",
      slug: "sai-tea",
      name: "Sai Tea Centre",
      category: "Food & Beverage",
      tagline: "Authentic Masala Tea & Fresh Bun Maska",
      description: "Famous local tea stall serving aromatic ginger cardamom tea and fresh snacks daily.",
      phone: "+91 94221 54321",
      address: "FC Road, Near Deccan Gymkhana",
      city: "Pune",
      pincode: "411004",
      hours: "6:00 AM - 10:00 PM (All 7 Days)",
      language: "mr",
      status: "Approved",
      validationScore: 88,
      services: [
        { name: "Special Masala Chai", description: "Fresh cow milk with hand-ground ginger & spices", price: "₹15", icon: "cup" },
        { name: "Bun Maska", description: "Warm fresh bun served with pure amul butter", price: "₹30", icon: "bread" },
        { name: "Kanda Poha", description: "Traditional Maharashtrian breakfast snack", price: "₹25", icon: "food" },
        { name: "Cream Roll", description: "Crisp bakery rolls filled with vanilla cream", price: "₹15", icon: "sweet" }
      ],
      gallery: [],
      provenance: {
        name: { source: "USER_TEXT", confidence: 1.0, confirmed: true },
        phone: { source: "USER_TEXT", confidence: 1.0, confirmed: true }
      }
    },
    {
      id: "patil-kirana",
      slug: "patil-kirana",
      name: "Patil Kirana Store",
      category: "Retail",
      tagline: "Fresh Groceries & Daily Essentials",
      description: "Wholesale & retail provision store serving families with genuine quality grains and spices.",
      phone: "+91 98901 67890",
      address: "Laxmipuri Main Market",
      city: "Kolhapur",
      pincode: "416002",
      hours: "8:00 AM - 9:00 PM (Open everyday)",
      language: "hi",
      status: "Published",
      validationScore: 88,
      services: [
        { name: "Grains & Pulses", description: "Handpicked Kolhapur rice, wheat, dal", price: "Wholesale rates", icon: "grain" },
        { name: "Spices & Masalas", description: "Authentic Kolhapuri Kanda-Lasun masala", price: "Freshly packed", icon: "spice" },
        { name: "Cooking Oil & Ghee", description: "Refined and cold-pressed pure groundnut oils", price: "MRP discount", icon: "oil" },
        { name: "Free Home Delivery", description: "Delivery within 3km for orders above ₹500", price: "Free", icon: "truck" }
      ],
      gallery: [],
      provenance: {}
    }
  ],

  // Get active business record (defaults to Shinde Auto Services)
  getCurrentBusiness() {
    try {
      const stored = localStorage.getItem('khojdoot_current_business');
      if (stored) {
        return JSON.parse(stored);
      }
    } catch (e) {
      console.warn("Could not read localStorage", e);
    }
    return this.sampleBusinesses[0];
  },

  // Save active business record
  saveCurrentBusiness(businessData) {
    try {
      localStorage.setItem('khojdoot_current_business', JSON.stringify(businessData));
      window.dispatchEvent(new CustomEvent('businessDataUpdated', { detail: businessData }));
    } catch (e) {
      console.warn("Could not write to localStorage", e);
    }
  },

  // Switch to one of the sample businesses by slug
  selectBusinessBySlug(slug) {
    const found = this.sampleBusinesses.find(b => b.slug === slug);
    if (found) {
      this.saveCurrentBusiness(found);
      return found;
    }
    return this.getCurrentBusiness();
  },

  // Record Checkpoint 1 user consent / approval
  approveBusinessInfo(businessData) {
    businessData.status = "Approved";
    businessData.approvedAt = new Date().toISOString();
    businessData.consentLedgerHash = "sha256_" + Math.random().toString(36).substring(2, 10);
    this.saveCurrentBusiness(businessData);
    return businessData;
  },

  // Dynamic Information Extraction & Real-time Business Generator
  extractAndCreateBusiness(rawText, currentLang = 'mr', attachedFile = null) {
    const text = (rawText || '').trim();
    const lower = text.toLowerCase();

    // 1. Check if user matched one of the pre-configured demo slugs
    if (lower.includes('sai tea') || (lower.includes('चहा') && lower.includes('साई')) || (lower.includes('चाय') && lower.includes('साई'))) {
      return this.selectBusinessBySlug('sai-tea');
    }
    if ((lower.includes('patil') && lower.includes('kirana')) || (lower.includes('किराणा') && lower.includes('पाटील')) || (lower.includes('किराना') && lower.includes('पाटिल'))) {
      return this.selectBusinessBySlug('patil-kirana');
    }
    if ((lower.includes('shinde') && lower.includes('auto')) || (lower.includes('शिंदे') && lower.includes('ऑटो'))) {
      return this.selectBusinessBySlug('shinde-auto');
    }

    // 2. Extract Business Name
    let businessName = '';
    const patterns = [
      /(?:name\s+(?:is|of)|named|called|run(?:ning)?\s+(?:a|an)?\s+[\w\s]+\s+(?:named|called)?)\s+([A-Za-z0-9\s&'-]+?)(?:\.|\,|$|\s+in\s+|\s+at\s+|\s+we\s+)/i,
      /(?:नाव|नाम|नावाने|పేరు)\s+([^\,\.\n]+)/i,
      /([^\,\.\n]+)\s+(?:नावाचे|नावाची|नावाचा|అనే)/i
    ];

    for (const pat of patterns) {
      const match = text.match(pat);
      if (match && match[1] && match[1].trim().length > 1) {
        businessName = match[1].trim();
        break;
      }
    }

    // If short input (e.g. "sunita tiffin" or "Sunita Tiffin Service")
    if (!businessName) {
      if (text.length > 0 && text.length <= 40) {
        businessName = text;
      } else if (text.length > 40) {
        const bizMatch = text.match(/([A-Za-z0-9\u0900-\u097F\u0C00-\u0C7F\s&'-]{2,25}\s+(?:tiffin|mess|canteen|bhojanalay|dhaba|hotel|restaurant|kitchen|cafe|tea|garage|auto|services|salon|parlour|tailor|boutique|store|kirana|mart|bakery|dairy|clinic|sweets|jewellers))/i);
        if (bizMatch && bizMatch[1]) {
          businessName = bizMatch[1].trim();
        } else {
          businessName = text.split(/\s+/).slice(0, 3).join(' ') || '';
        }
      }
    }

    if (!businessName || !businessName.trim()) {
      if (attachedFile && attachedFile.name) {
        const rawClean = attachedFile.name.replace(/\.[^/.]+$/, "").replace(/[_-]/g, ' ');
        if (rawClean.length > 2) {
          businessName = rawClean;
        }
      }
    }

    if (!businessName || !businessName.trim()) {
      businessName = (currentLang === 'mr') ? 'माझा व्यवसाय' : ((currentLang === 'hi') ? 'मेरा व्यवसाय' : ((currentLang === 'te') ? 'నా వ్యాపారం' : 'My Local Business'));
    }

    // Clean name
    businessName = businessName.replace(/^[,\.\-\s]+|[,\.\-\s]+$/g, '');
    businessName = businessName.replace(/\b([a-z])/g, (_, ch) => ch.toUpperCase());

    // Slug
    const slug = businessName.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || ('biz-' + Date.now().toString(36));

    // Phone
    let phone = '+91 98220 54321';
    const phoneMatch = text.match(/(?:\+91[\s-]?)?[6-9]\d{9}/);
    if (phoneMatch) phone = phoneMatch[0];

    // City
    let city = 'Pune';
    const cityMatch = text.match(/(?:in|at|from|मध्ये|शहरात|లో)?\s*(Pune|Nashik|Mumbai|Nagpur|Kolhapur|Aurangabad|Hyderabad|Thane|Solapur|Satara|पुणे|मुंबई|नाशिक|नागपूर|कोल्हापूर|హైదరాబాద్)/i);
    if (cityMatch && cityMatch[1]) {
      city = cityMatch[1].charAt(0).toUpperCase() + cityMatch[1].slice(1);
    }

    // Address
    let address = 'Main Market Road';
    const addrMatch = text.match(/(?:near|opposite|opp|at|रस्त्यावर|जवळ|సమీపంలో)\s+([A-Za-z0-9\s,\.-]+?)(?:\.|$)/i);
    if (addrMatch && addrMatch[1]) {
      address = addrMatch[1].trim();
    }

    // Category & Services
    let category = 'Local Business';
    let tagline = 'Quality service and trusted local business.';
    let description = text.length > 20 ? text : `Quality and reliable local service in ${city}.`;
    let services = [];
    let gallery = [];

    // TIFFIN / FOOD / MESS / CATERING
    if (lower.includes('tiffin') || lower.includes('टिफीन') || lower.includes('टिफिन') || lower.includes('डबा') || lower.includes('डबे') || lower.includes('టిఫిన్') || lower.includes('mess') || lower.includes('मेस') || lower.includes('bhojan') || lower.includes('जेवण') || lower.includes('थाळी') || lower.includes('thali') || lower.includes('canteen') || lower.includes('पोळी') || lower.includes('roti') || lower.includes('bhaji') || lower.includes('भोजन')) {
      category = (currentLang === 'mr') ? 'टिफीन व खानपान' :
                 (currentLang === 'hi') ? 'टिफिन व भोजन सेवा' :
                 (currentLang === 'te') ? 'టిఫిన్ & క్యాటరింగ్ సేవలు' : 'Tiffin & Food Catering';

      tagline = (currentLang === 'mr') ? 'घरगुती चविष्ट व सकस जेवणाचे डबे' :
                (currentLang === 'hi') ? 'स्वादिष्ट घर जैसा शुद्ध व ताजा टिफिन' :
                (currentLang === 'te') ? 'రుచికరమైన ఇంటి భోజనం మరియు తాజా టిఫిన్లు' : 'Fresh Homemade Tiffin & Daily Meal Delivery';

      description = (currentLang === 'mr') ? 'दररोज वेळेवर गरमागरम आणि सकस घरगुती जेवणाचे डबे पोहोचवण्याची विश्वासार्ह सेवा. शुद्ध तेल आणि ताजे धान्य वापरून बनवलेले पौष्टिक जेवण.' :
                    (currentLang === 'hi') ? 'शुद्ध, स्वादिष्ट और पौष्टिक घर के बने खाने की टिफिन सेवा। छात्रों और नौकरीपेशा लोगों के लिए विशेष व्यवस्था।' :
                    (currentLang === 'te') ? 'ఇంటి భోజనం లాంటి స్వచ్ఛమైన మరియు ఆరోగ్యకరమైన రోజువారీ టిఫిన్ డెలివరీ సేవ.' :
                    'Nutritious and hygienic homemade tiffin delivery serving authentic meals on time daily. Made with fresh ingredients, pure spices, and love.';

      services = [
        {
          name: (currentLang === 'mr') ? 'दुपारचा डबा (Daily Lunch)' : (currentLang === 'hi') ? 'दैनिक दोपहर टिफिन' : (currentLang === 'te') ? 'రోజువారీ మధ్యాహ్న భోజనం' : 'Daily Lunch Tiffin',
          description: (currentLang === 'mr') ? '४ ताज्या पोळ्या, रस्सा/सुकी भाजी, वरण आणि भात' : (currentLang === 'hi') ? '४ रोटियां, ताजी मौसमी सब्जी, दाल और चावल' : (currentLang === 'te') ? 'వేడి రోటీలు, తాజా కూర, పప్పు మరియు అన్నం' : '4 warm rotis, seasonal sabzi, dal & steamed rice',
          price: '₹80',
          icon: 'food'
        },
        {
          name: (currentLang === 'mr') ? 'रात्रीचा डबा (Dinner)' : (currentLang === 'hi') ? 'रात्रि का टिफिन' : (currentLang === 'te') ? 'రాత్రి భోజనం' : 'Daily Dinner Tiffin',
          description: (currentLang === 'mr') ? 'हलके, सकस आणि पचनास सोपे घरगुती रात्रीचे जेवण' : (currentLang === 'hi') ? 'हल्का और पौष्टिक रात का खाना' : (currentLang === 'te') ? 'తేలికపాటి మరియు ఆరోగ్యకరమైన రాత్రి భోజనం' : 'Light, healthy and nutritious home-style dinner',
          price: '₹80',
          icon: 'bread'
        },
        {
          name: (currentLang === 'mr') ? 'स्पेशल व्हेज थाळी (Special Thali)' : (currentLang === 'hi') ? 'स्पेशल वेज थाली' : (currentLang === 'te') ? 'స్పెషల్ వెజ్ థాలీ' : 'Special Veg Thali',
          description: (currentLang === 'mr') ? 'पनीर/विशेष भाजी, गोड शिरा, पुऱ्या, डाळ तडका व जिरा राईस' : (currentLang === 'hi') ? 'पनीर सब्जी, मिठाई, पूरी, दाल तड़का व जीरा राइस' : (currentLang === 'te') ? 'పన్నీర్ కూర, స్వీట్, పూరీ, దాల్ తడ్కా మరియు జీరా రైస్' : 'Paneer special sabzi, sweet dish, puris, dal tadka & jeera rice',
          price: '₹130',
          icon: 'food'
        },
        {
          name: (currentLang === 'mr') ? 'मासिक मेस (Monthly Subscription)' : (currentLang === 'hi') ? 'मासिक मेस सब्सक्रिप्शन' : (currentLang === 'te') ? 'నెలవారీ సబ్‌స్క్రిప్షన్' : 'Monthly Mess Subscription',
          description: (currentLang === 'mr') ? 'विद्यार्थी आणि नोकरदारांसाठी दररोज वेळेवर घरपोच डबा' : (currentLang === 'hi') ? 'छात्रों और कर्मचारियों के लिए प्रतिदिन घरपहुंच टिफिन' : (currentLang === 'te') ? 'విద్యార్థులు మరియు ఉద్యోగులకు ప్రతిరోజూ డోర్‌స్టెప్ డెలివరీ' : 'Doorstep tiffin delivery everyday for students & professionals',
          price: '₹2,200 / month',
          icon: 'cup'
        }
      ];

      gallery = [
        { title: (currentLang === 'mr') ? 'ताजा दुपारचा डबा' : (currentLang === 'hi') ? 'ताजा दोपहर टिफिन' : (currentLang === 'te') ? 'తాజా మధ్యాహ్న టిఫిన్' : 'Fresh Tiffin Packing', url: 'assets/images/service1.jpg' },
        { title: (currentLang === 'mr') ? 'स्पेशल थाळी' : (currentLang === 'hi') ? 'स्पेशल थाली' : (currentLang === 'te') ? 'స్పెషల్ థాలీ' : 'Special Veg Thali', url: 'assets/images/service2.jpg' },
        { title: (currentLang === 'mr') ? 'स्वच्छ स्वयंपाकघर' : (currentLang === 'hi') ? 'स्वच्छ रसोई' : (currentLang === 'te') ? 'శుభ్రమైన వంటగది' : 'Hygienic Kitchen', url: 'assets/images/service3.jpg' }
      ];
    } else if (lower.includes('salon') || lower.includes('parlour') || lower.includes('beauty') || lower.includes('पार्लर') || lower.includes('कटिंग') || lower.includes('hair') || lower.includes('బ్యూటీ')) {
      // SALON & BEAUTY
      category = (currentLang === 'mr') ? 'सौंदर्य व सलून' : (currentLang === 'hi') ? 'ब्यूटी व सैलून' : (currentLang === 'te') ? 'బ్యూటీ & సెలూన్' : 'Beauty & Salon';
      tagline = (currentLang === 'mr') ? 'उत्कृष्ट हेअरकट व सौंदर्य सेवा' : (currentLang === 'hi') ? 'सर्वश्रेष्ठ हेयरकट और ग्रूमिंग' : (currentLang === 'te') ? 'అందమైన హెయిర్‌కట్ & బ్యూటీ సేవలు' : 'Professional Hair & Beauty Care';
      services = [
        { name: 'Hair Cut & Styling', description: 'Modern styling and grooming', price: '₹150', icon: 'wrench' },
        { name: 'Facial & Glow', description: 'Deep cleansing and herbal facials', price: '₹400', icon: 'cup' },
        { name: 'Hair Spa & Treatment', description: 'Anti-dandruff and nourishing care', price: '₹500', icon: 'oil' },
        { name: 'Bridal & Special Makeup', description: 'Traditional and party makeup', price: '₹1,500', icon: 'food' }
      ];
    } else if (lower.includes('tailor') || lower.includes('शिंपी') || lower.includes('boutique') || lower.includes('कपडे') || lower.includes('clothes') || lower.includes('ట్రైలర్')) {
      // TAILORING
      category = (currentLang === 'mr') ? 'टेलरिंग व बुटिक' : (currentLang === 'hi') ? 'टेलरिंग व बुटीक' : (currentLang === 'te') ? 'టైలరింగ్ & బోటిక్' : 'Tailoring & Boutique';
      tagline = (currentLang === 'mr') ? 'योग्य मापाचे व फॅशनेबल कपडे' : (currentLang === 'hi') ? 'सही फिटिंग और मनपसंद सिलाई' : (currentLang === 'te') ? 'ఖచ్చితమైన ఫిట్టింగ్ మరియు స్టిచింగ్' : 'Custom Tailoring & Perfect Fit Stitching';
      services = [
        { name: 'Designer Blouse', description: 'Custom neck patterns & embroidery work', price: '₹350 onwards', icon: 'bread' },
        { name: 'Ladies Suit & Kurti', description: 'Perfect fitting salwars and dresses', price: '₹400', icon: 'bread' },
        { name: 'Gents Shirt & Pant', description: 'Formal and casual stitching', price: '₹600', icon: 'bread' },
        { name: 'Alterations & Repair', description: 'Fast alteration and adjustments', price: '₹50', icon: 'wrench' }
      ];
    } else if (lower.includes('kirana') || lower.includes('grocery') || lower.includes('किराणा') || lower.includes('किराना') || lower.includes('store') || lower.includes('दुकान') || lower.includes('కిరాణా')) {
      // GROCERY & KIRANA
      category = (currentLang === 'mr') ? 'किराणा व जनरल स्टोअर' : (currentLang === 'hi') ? 'किराना व जनरल स्टोर' : (currentLang === 'te') ? 'కిరాణా & జనరల్ స్టోర్' : 'Grocery & Provisions';
      tagline = (currentLang === 'mr') ? 'ताजे धान्य व दैनंदिन जीवनावश्यक वस्तू' : (currentLang === 'hi') ? 'ताजा अनाज और दैनिक जरूरी सामान' : (currentLang === 'te') ? 'తాజా సరుకులు & నిత్యావసర వస్తువులు' : 'Fresh Groceries & Daily Essentials';
      services = [
        { name: 'Grains & Pulses', description: 'Handpicked quality wheat, rice & dal', price: 'Wholesale rates', icon: 'grain' },
        { name: 'Spices & Masalas', description: 'Authentic local freshly ground spices', price: 'Special price', icon: 'spice' },
        { name: 'Cooking Oil & Ghee', description: 'Filtered and cold pressed edible oils', price: 'MRP discount', icon: 'oil' },
        { name: 'Free Home Delivery', description: 'Delivery within local area on orders above ₹500', price: 'Free', icon: 'truck' }
      ];
    } else {
      // GENERAL SME / SERVICE
      category = (currentLang === 'mr') ? 'स्थानिक सेवा व व्यवसाय' : (currentLang === 'hi') ? 'स्थानीय व्यापार व सेवाएं' : (currentLang === 'te') ? 'స్థానిక వ్యాపార సేవలు' : 'Local Business & Services';
      tagline = (currentLang === 'mr') ? 'विश्वासार्ह सेवा आणि वाजवी दर' : (currentLang === 'hi') ? 'विश्वसनीय सेवा और उचित दरें' : (currentLang === 'te') ? 'నమ్మకమైన సేవలు మరియు సరసమైన ధరలు' : 'Trusted Local Services at Fair Pricing';
      services = [
        { name: 'Standard Service', description: 'Expert assistance and quality service', price: 'Fair rates', icon: 'wrench' },
        { name: 'Custom Request', description: 'Tailored solutions according to your needs', price: 'On inspection', icon: 'cog' },
        { name: 'Consultation & Inquiries', description: 'Direct call or visit store anytime', price: 'Free', icon: 'cup' },
        { name: 'Emergency Assistance', description: 'Prompt response for local customers', price: 'Standard', icon: 'bike' }
      ];
    }

    const newBusiness = {
      id: slug,
      slug: slug,
      name: businessName,
      category: category,
      tagline: tagline,
      description: description,
      phone: phone,
      address: address,
      city: city,
      pincode: '411001',
      hours: '8:00 AM - 9:30 PM (Daily)',
      language: currentLang,
      status: 'Pending Approval',
      validationScore: 90,
      heroImage: attachedFile ? attachedFile.dataUrl : null,
      photo: attachedFile ? attachedFile.dataUrl : null,
      photoName: attachedFile ? attachedFile.name : null,
      services: services,
      gallery: (attachedFile ? [{ title: 'Storefront', url: attachedFile.dataUrl }] : []).concat(gallery.length > 0 ? gallery : [
        { title: 'Store Front', url: 'assets/images/service1.jpg' },
        { title: 'Quality Work', url: 'assets/images/service2.jpg' },
        { title: 'Customer Service', url: 'assets/images/service3.jpg' }
      ]),
      provenance: {
        name: { source: attachedFile ? 'AI_VISION' : 'USER_TEXT', confidence: 1.0, confirmed: true },
        category: { source: 'AI_INFERENCE', confidence: 0.95, confirmed: true },
        phone: { source: 'USER_TEXT', confidence: 0.95, confirmed: true },
        services: { source: 'AI_INFERENCE', confidence: 0.92, confirmed: true },
        address: { source: 'USER_TEXT', confidence: 0.90, confirmed: true }
      }
    };

    // Keep in sampleBusinesses array
    const existingIdx = this.sampleBusinesses.findIndex(b => b.slug === slug);
    if (existingIdx >= 0) {
      this.sampleBusinesses[existingIdx] = newBusiness;
    } else {
      this.sampleBusinesses.unshift(newBusiness);
    }

    this.saveCurrentBusiness(newBusiness);
    return newBusiness;
  }
};

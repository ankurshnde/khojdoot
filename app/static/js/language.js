/**
 * KhojDoot Regional Language System
 * Pure single-language translations for:
 * - English ('en')
 * - Marathi ('mr')
 * - Hindi ('hi')
 * - Telugu ('te') - Added for Hyderabad Hackathon
 * 
 * Designed for Gayatri's KhojDoot Frontend
 */

const KhojLanguage = {
  currentLanguage: 'mr', // Default language
  
  translations: {
    // =======================================================================
    // 100% PURE ENGLISH (No Marathi or other languages mixed in)
    // =======================================================================
    en: {
      brandName: 'KhojDoot',
      betaBadge: 'Beta',
      
      // Navigation
      navChat: 'Chat',
      navApproval: 'Approval',
      navPreview: 'Preview',
      navEditor: 'Editor',
      navMerchant: 'Merchant Site',
      navLabs: 'Labs',
      
      // Main Chat / Input
      tellUsTitle: 'Tell us about your business',
      tellUsSubtitle: "You can type, speak, or share photos. We'll create your website automatically.",
      inputLangLabel: 'Language:',
      promptPlaceholder: 'Describe your business in your own language...',
      tryExample: 'Examples:',
      exampleTiffin: 'Sunita Tiffin Service',
      exampleTea: 'I run a tea shop',
      exampleGarage: 'I have a car garage',
      exampleHandmade: 'I sell handmade products',
      
      // Sample prompt texts
      sampleTiffinText: "I run a tiffin service named Sunita Tiffin in Pune. We deliver fresh homemade lunch and dinner meals daily.",
      sampleTeaText: "I run a tea shop named Sai Tea Centre. We serve fresh masala chai and bun maska.",
      sampleGarageText: "I run a car and bike garage in Nashik named Shinde Auto Services. We do servicing, repairs, and oil change.",
      sampleHandmadeText: "I sell handmade gift items and traditional crafts.",
      
      // Buttons & Controls
      btnSend: 'Send',
      btnVoice: 'Voice Input',
      btnImage: 'Upload Photo',
      btnAttach: 'Attach File',
      btnStop: 'Stop',
      btnRemove: 'Remove',
      btnReset: 'New Chat',
      btnApprove: 'Approve Information',
      btnSave: 'Save Changes',
      btnBackChat: 'Back to Chat',
      btnBackApproval: 'Back to Approval',
      btnProceedPreview: 'View Website Preview',
      btnOpenEditor: 'Open Editor',
      btnPublish: 'Publish Website',
      btnCallNow: 'Call Now',
      btnAddService: '+ Add Service',
      btnUploadPhoto: 'Upload Photo',
      btnDirections: 'Directions & Hours',
      btnOpenSplitPreview: '👁️ Open Live Preview Beside Chat',
      previewToggleOn: 'Preview: On',
      previewToggleOff: 'Preview: Off',
      step1Approval: 'Step 1: Review & Approve Info',
      step2Preview: 'Step 2: View Website Preview',
      step3Editor: 'Step 3: Open Website Editor',
      step4Merchant: 'Step 4: Visit Live Merchant Site',
      
      // Bot Messages
      botWelcome: 'Hello! What is your shop or business name, and what services do you offer?',
      botAck: 'Thank you! I have captured your business details for',
      botVoiceAck: 'Voice note received and transcribed successfully.',
      botImageAck: 'Photo received and business details extracted successfully.',
      readyForApproval: 'Your business details are ready for review.',
      reviewInfoBtn: 'Review Information →',
      
      // Status & Badges
      statusLiveChat: 'Live Chat',
      statusPending: 'Pending Approval',
      statusApproved: 'Approved',
      statusHealthy: 'System Healthy',
      statusLivePreview: 'Live Preview',
      statusVerified: 'Verified Local Business',
      
      // Business Approval Form
      checkpoint1Title: 'Business Information Approval',
      checkpoint1Desc: 'Please review your extracted business details below. You can edit any field before approving.',
      approvalSuccessMsg: 'Business information approved successfully! Website generation is ready.',
      labelShopName: 'Business Name',
      labelCategory: 'Category',
      labelTagline: 'Headline / Tagline',
      labelPhone: 'Phone Number',
      labelAddress: 'Shop Address',
      labelCity: 'City',
      labelHours: 'Working Hours',
      labelDescription: 'Business Description',
      labelServicesTitle: 'Products and Services',
      labelServicesDesc: 'List of services and products available for customers.',
      labelGalleryTitle: 'Shop Photos & Gallery',
      labelGalleryDesc: 'Photos of your shop, board, and products.',
      labelPhoto: 'Business Photo / Board',
      noPhotoAttached: 'No photo attached yet',
      btnChangePhoto: '+ Add / Change Photo',
      
      // Website Preview & Components
      checkpoint2Title: 'Website Preview',
      checkpoint2Desc: 'Inspect your generated website. It updates instantly when you edit.',
      mockNavHome: 'Home',
      mockNavServices: 'Services',
      mockNavGallery: 'Gallery',
      mockNavContact: 'Contact',
      ourServices: 'Our Services',
      servicesSubtitle: 'Quality services offered at fair prices.',
      galleryTitle: 'Photo Gallery',
      gallerySubtitle: 'Glimpses of our store, equipment, and recent work.',
      contactTitle: 'Contact & Location',
      contactSubtitle: 'Visit our store or call us directly.',
      cardAddress: 'Store Address',
      cardPhone: 'Direct Call',
      cardHours: 'Working Hours',
      openMaps: 'Open in Google Maps ↗',
      callAvailable: 'Open for calls today',
      footerRights: 'All rights reserved. Powered by KhojDoot.',
      footerCopyright: 'All rights reserved. Powered by KhojDoot.',
      
      // Showcase Shinde Auto Texts
      heroTitleShinde: 'Reliable Car & Bike Service in Nashik',
      heroDescShinde: 'Quality service. Fair pricing. Trusted by locals for 15+ years.',
      svcCarTitle: 'Car Service',
      svcCarDesc: 'Periodic & general maintenance, oil and brake checks',
      svcBikeTitle: 'Bike Service',
      svcBikeDesc: 'All two wheeler tune-up and engine servicing',
      svcRepairsTitle: 'Repairs',
      svcRepairsDesc: 'Engine overhaul, electrical and brake repairs',
      svcOilTitle: 'Oil Change',
      svcOilDesc: 'All major synthetic and engine oil brands',
      galleryWorkshop: 'Workshop & Tools',
      galleryDiagnostics: 'Diagnostics & Inspection',
      galleryParts: 'Genuine Spare Parts',
      
      // Website Editor
      editorTitle: 'Website Editor',
      editorSubtitle: 'Customize business details, colors, and sections with instant live preview.',
      tabContent: 'Content',
      tabTheme: 'Colors & Theme',
      tabSections: 'Sections',
      labelThemeColor: 'Primary Brand Color',
      labelFont: 'Typography Font',
      labelSectionVisibility: 'Section Visibility (Show / Hide)',
      secHeader: 'Navigation Header',
      secHero: 'Hero Banner',
      secServices: 'Services & Products',
      secGallery: 'Photo Gallery',
      secContact: 'Contact & Location',
      secFooter: 'Footer',
      
      // Merchant Page
      merchantTitle: 'Official Merchant Website',
      merchantSubtitle: 'Verified Digital Web Presence by KhojDoot',
      selectMerchant: 'Select Shop:',
      
      // Toast notifications
      toastLangChanged: 'Language changed to English',
      toastSaved: 'Changes saved successfully',
      toastApproved: 'Business information approved',

      // Front Page Login & Verification Gate
      loginTitle: 'Welcome to KhojDoot',
      loginSubtitle: 'Enter your name and 10-digit mobile number to create your business website.',
      labelYourName: 'Your Name *',
      placeholderName: 'e.g. Rahul Patil or Sunita Shinde',
      labelMobileNumber: '10-Digit Mobile Number *',
      placeholderPhone: '10-digit mobile number (e.g. 9822012345)',
      errPhone10Digits: '⚠️ Please enter a valid 10-digit mobile number.',
      btnSendOtpText: 'Send OTP →',
      otpSentBanner: 'OTP has been sent to your number! Demo OTP:',
      labelEnterOtp: 'Enter 4-Digit OTP',
      errOtpInvalid: '⚠️ Invalid OTP! Please enter the correct 4-digit code.',
      btnVerifyText: 'Verify ✓',
      userChangeBtn: 'Change',
      userProfileDefault: 'Merchant',

      // Workspace & Main Chat
      navCreate: 'Create / Chat',
      greetingHello: 'Hello',
      botWelcomeMsg: 'Hello! What is your shop or business name, and what services do you provide? You can tell us by typing, speaking, or sharing photos.',
      voiceListening: 'Voice Typing (Listening...)',
      voiceMicActive: 'Mic is active...',
      btnStopVoice: 'Stop ✕',
      photoAttachedBadge: 'Photo attached ✓',
      promptPlaceholderText: 'Describe your business in your language or click the mic to speak...',
      examplesLabel: 'Examples (or choose one):',
      chipTiffinLabel: '🍱 Sunita Tiffin Service (Pune)',
      chipTeaLabel: '☕ Sai Tea Centre (Pune)',
      chipGarageLabel: '🚗 Shinde Auto Services (Nashik)',
      chipKiranaLabel: '🧵 Patil Grocery & Essentials',

      // Side-by-Side Business Summary (Checkpoint 1)
      sumTitle: '📋 Business Summary',
      sumSubtitle: 'Please review the details below and grant approval',
      sumLabelBizName: 'Business Name:',
      sumLabelOwner: 'Owner Name:',
      sumLabelPhone: 'Mobile Number:',
      sumLabelCategory: 'Category:',
      sumLabelLocation: 'Address & City:',
      sumLabelHours: 'Working Hours:',
      sumLabelTagline: 'Tagline:',
      sumLabelServicesHeader: 'Offered Services & Pricing:',
      btnApproveLabel: '✓ Approved',
      btnRejectLabel: '✕ Not approved',
      btnBackLabel: '← Back',

      // Strict Preview Gate (Locked)
      gateLockTitle: 'Website Preview is Locked',
      gateLockDesc: 'To display the live website preview and start editing, please click "Approved" on the business summary above.',

      // Unified Live Website Preview & Voice-Typing Editor
      previewLiveBadge: '● Live Preview',
      btnPublishText: 'Publish ↗',
      editorVoiceTitle: '🎙️ Edit by Voice or Chat',
      editorLiveBadge: 'Live Editor',
      editorHelpText: "You can speak or type commands like: 'Change theme to saffron', 'Add car wash service for ₹299', or 'Change hours from 9 AM to 9 PM'.",
      editorPlaceholder: 'Tell or type what changes you want to make in your website...',
      editorMicPrompt: 'Click mic to speak',
      editorPillSaffron: '🟠 Saffron Theme',
      editorPillBlue: '🔵 Blue Theme',
      editorPillGreen: '🟢 Green Theme',
      editorPillService: '➕ Add Service (₹299)',
      editorPillGallery: '🖼️ Hide Gallery',
      editorColorChoose: 'Choose Theme Color:',
      botSummaryNotice: "Thank you! I have extracted your business details. Please review the Business Summary on the right and click 'Approved'.",
      botApprovedNotice: 'Congratulations! Information approved. Your live website is displayed on the right. You can make changes anytime by voice typing or chat below!',
      botRejectedNotice: 'You have requested corrections. Please tell or type what changes are needed in your business details.',
      toastOtpSuccess: 'OTP verified successfully! Welcome.',
      toastOtpSent: 'OTP sent successfully: ',
      toastApprovedMsg: 'Business details approved! Live website preview is ready.',
      toastVoiceTranscribed: 'Voice transcribed ✓',
      toastEditApplied: 'Changes applied successfully'
    },
    
    // =======================================================================
    // 100% PURE MARATHI (मराठी)
    // =======================================================================
    mr: {
      brandName: 'KhojDoot',
      betaBadge: 'बीटा',
      
      // Navigation
      navChat: 'चॅट',
      navApproval: 'मंजुरी',
      navPreview: 'पूर्वावलोकन',
      navEditor: 'संपादक',
      navMerchant: 'व्यापारी साइट',
      navLabs: 'लॅब्स',
      
      // Main Chat / Input
      tellUsTitle: 'तुमच्या व्यवसायाबद्दल सांगा',
      tellUsSubtitle: 'तुम्ही टाइप करू शकता, बोलू शकता किंवा फोटो पाठवू शकता. आम्ही तुमची वेबसाइट आपोआप तयार करू.',
      inputLangLabel: 'भाषा:',
      promptPlaceholder: 'तुमच्या भाषेत व्यवसायाची माहिती लिहा...',
      tryExample: 'उदाहरणे:',
      exampleTiffin: 'सुनिता टिफिन सेवा',
      exampleTea: 'माझे चहाचे दुकान आहे',
      exampleGarage: 'माझे कार व बाईक गॅरेज आहे',
      exampleHandmade: 'मी हस्तकला वस्तू विकतो',
      
      // Sample prompt texts
      sampleTiffinText: 'माझे पुण्यात सुनिता टिफिन नावाचे घरगुती जेवणाचे डबे देण्याचे काम आहे. आम्ही रोज ताजे आणि सकस जेवण घरपोच देतो.',
      sampleTeaText: 'माझे चहाचे दुकान आहे, नाव साई टी सेंटर. आम्ही गरमागरम मसाला चहा आणि ताजे बन मस्का देतो.',
      sampleGarageText: 'माझे नाशिकमध्ये कार आणि बाईक गॅरेज आहे, नाव शिंदे ऑटो सर्व्हिसेस. आम्ही सर्व्हिसिंग, ऑइल चेंज आणि दुरुस्ती करतो.',
      sampleHandmadeText: 'मी घरगुती हस्तकला वस्तू आणि पारंपरिक भेटवस्तू विकतो.',
      
      // Buttons & Controls
      btnSend: 'पाठवा',
      btnVoice: 'आवाज इनपुट',
      btnImage: 'फोटो जोडा',
      btnAttach: 'फाइल जोडा',
      btnStop: 'थांबवा',
      btnRemove: 'काढून टाका',
      btnReset: 'नवीन चॅट',
      btnApprove: 'माहिती मंजूर करा',
      btnSave: 'बदल जतन करा',
      btnBackChat: 'चॅटकडे परत जा',
      btnBackApproval: 'माहितीकडे परत जा',
      btnProceedPreview: 'वेबसाइट पूर्वावलोकन पहा',
      btnOpenEditor: 'संपादक उघडा',
      btnPublish: 'वेबसाइट प्रसिद्ध करा',
      btnCallNow: 'कॉल करा',
      btnAddService: '+ नवीन सेवा जोडा',
      btnUploadPhoto: 'फोटो जोडा',
      btnDirections: 'पत्ता आणि वेळा',
      btnOpenSplitPreview: '👁️ बाजूला थेट पूर्वावलोकन उघडा',
      previewToggleOn: 'पूर्वावलोकन: चालू',
      previewToggleOff: 'पूर्वावलोकन: बंद',
      step1Approval: 'पायरी १: माहिती मंजुरी',
      step2Preview: 'पायरी २: वेबसाइट पूर्वावलोकन',
      step3Editor: 'पायरी ३: वेबसाइट संपादक',
      step4Merchant: 'पायरी ४: अधिकृत व्यापारी साइट',
      
      // Bot Messages
      botWelcome: 'नमस्कार! तुमच्या दुकानाचे किंवा व्यवसायाचे नाव काय आहे आणि तुम्ही कोणत्या सेवा पुरवता?',
      botAck: 'धन्यवाद! मी तुमच्या व्यवसायाची माहिती नोंदवून घेतली आहे:',
      botVoiceAck: 'तुमचा आवाज प्राप्त झाला आणि माहिती मजकुरात रूपांतरित झाली.',
      botImageAck: 'फोटो प्राप्त झाला आणि त्यातील व्यवसाय माहिती काढली गेली.',
      readyForApproval: 'तुमची व्यवसाय माहिती तपासणीसाठी तयार आहे.',
      reviewInfoBtn: 'माहिती तपासा →',
      
      // Status & Badges
      statusLiveChat: 'थेट चॅट',
      statusPending: 'मंजुरी प्रलंबित',
      statusApproved: 'मंजूर',
      statusHealthy: 'प्रणाली कार्यरत',
      statusLivePreview: 'थेट पूर्वावलोकन',
      statusVerified: 'स्थानिक स्तरावर पडताळणी झालेला व्यवसाय',
      
      // Business Approval Form
      checkpoint1Title: 'व्यवसाय माहिती मंजुरी',
      checkpoint1Desc: 'कृपया खालील व्यवसाय माहिती तपासा. गरज असल्यास तुम्ही कोणताही मजकूर बदलू शकता.',
      approvalSuccessMsg: 'व्यवसाय माहिती मंजूर झाली आहे! आता वेबसाइट तयार करण्यासाठी तयार आहे.',
      labelShopName: 'दुकानाचे नाव',
      labelCategory: 'व्यवसाय वर्ग',
      labelTagline: 'शीर्षक / ब्रीदवाक्य',
      labelPhone: 'फोन नंबर',
      labelAddress: 'दुकानाचा पत्ता',
      labelCity: 'शहर',
      labelHours: 'कामाच्या वेळा',
      labelDescription: 'व्यवसायाचे वर्णन',
      labelServicesTitle: 'उत्पादने आणि सेवा',
      labelServicesDesc: 'ग्राहकांसाठी उपलब्ध असणाऱ्या सर्व वस्तू किंवा सेवांची यादी.',
      labelGalleryTitle: 'दुकानाची छायाचित्रे',
      labelGalleryDesc: 'दुकान पाटी, कार्यशाळा आणि उत्पादनांचे फोटो.',
      labelPhoto: 'व्यवसाय फोटो / बोर्ड',
      noPhotoAttached: 'अद्याप कोणताही फोटो जोडलेला नाही',
      btnChangePhoto: '+ फोटो बदला / जोडा',
      
      // Website Preview & Components
      checkpoint2Title: 'वेबसाइट पूर्वावलोकन',
      checkpoint2Desc: 'तयार झालेली वेबसाइट तपासा. बदल केल्यास येथे तात्काळ बदल दिसतील.',
      mockNavHome: 'मुख्य',
      mockNavServices: 'सेवा',
      mockNavGallery: 'छायाचित्रे',
      mockNavContact: 'संपर्क',
      ourServices: 'आमच्या सेवा',
      servicesSubtitle: 'आमच्या दुकानातून मिळणाऱ्या सर्व प्रमुख सेवा आणि वाजवी दर.',
      galleryTitle: 'छायाचित्रे',
      gallerySubtitle: 'कामाचा दर्जा आणि कार्यशाळेची छायाचित्रे.',
      contactTitle: 'संपर्क आणि पत्ता',
      contactSubtitle: 'कधीही भेट द्या किंवा थेट फोनवरून चौकशी करा.',
      cardAddress: 'दुकानाचा पत्ता',
      cardPhone: 'थेट संपर्क',
      cardHours: 'कामाच्या वेळा',
      openMaps: 'गुगल मॅप्सवर पहा ↗',
      callAvailable: 'आज कॉलसाठी उपलब्ध',
      footerRights: 'सर्व हक्क राखीव. खोजदूत प्रणालीद्वारे संचलित.',
      footerCopyright: 'सर्व हक्क राखीव. खोजदूत प्रणालीद्वारे संचलित.',
      
      // Showcase Shinde Auto Texts
      heroTitleShinde: 'नाशिकमधील विश्वासार्ह कार आणि बाईक सर्व्हिस',
      heroDescShinde: 'उत्कृष्ट सेवा. योग्य दर. 15 वर्षांहून अधिक काळ स्थानिक लोकांचा विश्वास.',
      svcCarTitle: 'कार सर्व्हिस',
      svcCarDesc: 'नियमित आणि सर्वसाधारण देखभाल, ऑइल आणि ब्रेक तपासणी',
      svcBikeTitle: 'बाईक सर्व्हिस',
      svcBikeDesc: 'सर्व टू-व्हीलर सर्व्हिसिंग आणि इंजिन ट्यून-अप',
      svcRepairsTitle: 'दुरुस्ती',
      svcRepairsDesc: 'इंजिन, ब्रेक आणि वायरिंग दुरुस्ती',
      svcOilTitle: 'ऑइल बदल',
      svcOilDesc: 'सर्व नामांकित सिंथेटिक आणि इंजिन ऑइल ब्रँड्स',
      galleryWorkshop: 'कार्यशाळा व साधने',
      galleryDiagnostics: 'इंजिन व ब्रेक तपासणी',
      galleryParts: 'अस्सल सुटे भाग',
      
      // Website Editor
      editorTitle: 'वेबसाइट संपादक',
      editorSubtitle: 'व्यवसाय तपशील, रंग आणि विभाग थेट बदला. बदल उजवीकडे तात्काळ दिसतील.',
      tabContent: 'मजकूर',
      tabTheme: 'रंग आणि शैली',
      tabSections: 'विभाग',
      labelThemeColor: 'मुख्य ब्रँड रंग',
      labelFont: 'अक्षर शैली',
      labelSectionVisibility: 'विभाग दाखवा किंवा लपवा',
      secHeader: 'नेव्हिगेशन हेडर',
      secHero: 'हिरो बॅनर',
      secServices: 'सेवा आणि उत्पादने',
      secGallery: 'छायाचित्रे गॅलरी',
      secContact: 'पत्ता आणि संपर्क',
      secFooter: 'तळटीप',
      
      // Merchant Page
      merchantTitle: 'अधिकृत व्यापारी वेबसाइट',
      merchantSubtitle: 'खोजदूत प्रमाणित डिजिटल वेब उपस्थिती',
      selectMerchant: 'दुकान निवडा:',
      
      // Toast notifications
      toastLangChanged: 'भाषा मराठी निवडली',
      toastSaved: 'बदल यशस्वीपणे जतन झाले',
      toastApproved: 'व्यवसाय माहिती मंजूर झाली',

      // Front Page Login & Verification Gate
      loginTitle: 'खोजदूत मध्ये आपले स्वागत आहे',
      loginSubtitle: 'आपल्या व्यवसायाची सुंदर वेबसाइट तयार करण्यासाठी आपले नाव आणि 10 अंकी मोबाइल नंबर प्रविष्ट करा.',
      labelYourName: 'आपले नाव *',
      placeholderName: 'उदा. राहुल पाटील किंवा सुनिता शिंदे',
      labelMobileNumber: '10 अंकी मोबाइल नंबर *',
      placeholderPhone: '10 अंकी मोबाइल नंबर (उदा. 9822012345)',
      errPhone10Digits: '⚠️ कृपया बरोबर 10 अंकी मोबाइल नंबर प्रविष्ट करा.',
      btnSendOtpText: 'ओटीपी पाठवा (Send OTP) →',
      otpSentBanner: 'ओटीपी तुमच्या नंबरवर पाठवला आहे! डेमो OTP:',
      labelEnterOtp: '4 अंकी ओटीपी टाका',
      errOtpInvalid: '⚠️ अवैध ओटीपी! कृपया बरोबर 4 अंकी कोड प्रविष्ट करा.',
      btnVerifyText: 'Verify ✓',
      userChangeBtn: 'बदला',
      userProfileDefault: 'व्यापारी',

      // Workspace & Main Chat
      navCreate: 'तयार करा / चॅट',
      greetingHello: 'नमस्कार,',
      botWelcomeMsg: 'नमस्कार! तुमच्या दुकानाचे किंवा व्यवसायाचे नाव काय आहे आणि तुम्ही कोणत्या सेवा पुरवता? तुम्ही बोलून किंवा फोटो देऊनही सांगू शकता.',
      voiceListening: 'बोलत राहा (Voice Typing...)',
      voiceMicActive: 'माईक चालू आहे...',
      btnStopVoice: 'थांबवा ✕',
      photoAttachedBadge: 'फोटो जोडला आहे ✓',
      promptPlaceholderText: 'तुमच्या भाषेत व्यवसायाची माहिती लिहा किंवा बोला...',
      examplesLabel: 'उदाहरणे (किंवा यापैकी निवडा):',
      chipTiffinLabel: '🍱 सुनिता टिफिन सेवा (पुणे)',
      chipTeaLabel: '☕ साई चहा सेंटर (पुणे)',
      chipGarageLabel: '🚗 शिंदे ऑटो सर्व्हिसेस (नाशिक)',
      chipKiranaLabel: '🧵 पाटील किराणा व वस्तू',

      // Side-by-Side Business Summary (Checkpoint 1)
      sumTitle: '📋 व्यवसाय सारांश',
      sumSubtitle: 'कृपया खालील माहिती तपासून मंजुरी द्या',
      sumLabelBizName: 'व्यवसायाचे नाव:',
      sumLabelOwner: 'मालकाचे नाव:',
      sumLabelPhone: 'मोबाइल नंबर:',
      sumLabelCategory: 'श्रेणी (Category):',
      sumLabelLocation: 'पत्ता व शहर:',
      sumLabelHours: 'कामाच्या वेळा:',
      sumLabelTagline: 'टॅगलाइन:',
      sumLabelServicesHeader: 'पुरवल्या जाणाऱ्या सेवा व दर:',
      btnApproveLabel: '✓ Approved (मंजूर आहे)',
      btnRejectLabel: '✕ Not approved (मंजूर नाही)',
      btnBackLabel: '← Back (मागे जा)',

      // Strict Preview Gate (Locked)
      gateLockTitle: 'वेबसाइट पूर्वावलोकन कुलूपबंद आहे',
      gateLockDesc: 'वेबसाइटचे थेट पूर्वावलोकन आणि संपादन सुरू करण्यासाठी वरील व्यवसाय सारांशात "Approved" बटनावर क्लिक करा.',

      // Unified Live Website Preview & Voice-Typing Editor
      previewLiveBadge: '● थेट पूर्वावलोकन',
      btnPublishText: 'प्रसिद्ध करा ↗',
      editorVoiceTitle: '🎙️ बोलून किंवा चॅटने बदल करा',
      editorLiveBadge: 'थेट संपादन',
      editorHelpText: 'तुम्ही आवाजाने बोलू शकता जसे की: "थीम रंग भगवा करा", "कार वॉश सेवा 299 रुपयांना जोडा", किंवा "कामाच्या वेळा सकाळी 9 ते रात्री 9 करा".',
      editorPlaceholder: 'वेबसाइटमध्ये काय बदल करायचे आहेत ते सांगा किंवा लिहा...',
      editorMicPrompt: 'माईक वर क्लिक करा',
      editorPillSaffron: '🟠 भगवा थीम (Saffron)',
      editorPillBlue: '🔵 निळा थीम (Blue)',
      editorPillGreen: '🟢 हिरवा थीम (Green)',
      editorPillService: '➕ सेवा जोडा (₹299)',
      editorPillGallery: '🖼️ गॅलरी लपवा',
      editorColorChoose: 'थीम रंग निवडा:',
      botSummaryNotice: "धन्यवाद! मी तुमच्या व्यवसायाची माहिती गोळा केली आहे. कृपया उजव्या बाजूला दिलेला व्यवसाय सारांश तपासा आणि 'Approved' बटनावर क्लिक करा.",
      botApprovedNotice: 'अभिनंदन! माहिती मंजूर झाली आहे. तुमची थेट वेबसाइट उजव्या बाजूला प्रदर्शित केली आहे. तुम्ही खाली बोलून किंवा टाइप करून हवे ते बदल करू शकता!',
      botRejectedNotice: 'तुम्ही सारांश नामंजूर केला आहे. नावामध्ये, फोनमध्ये किंवा सेवांमध्ये काय दुरुस्ती करायची आहे ते खाली बोलून किंवा लिहून सांगा.',
      toastOtpSuccess: 'ओटीपी पडताळणी यशस्वी! आपले स्वागत आहे.',
      toastOtpSent: 'ओटीपी पाठवला आहे: ',
      toastApprovedMsg: 'व्यवसाय माहिती मंजूर झाली! वेबसाइट पूर्वावलोकन तयार आहे.',
      toastVoiceTranscribed: 'आवाज टाइप केला गेला ✓',
      toastEditApplied: 'बदल लागू झाले'
    },
    
    // =======================================================================
    // 100% PURE HINDI (हिंदी)
    // =======================================================================
    hi: {
      brandName: 'KhojDoot',
      betaBadge: 'बीटा',
      
      // Navigation
      navChat: 'चैट',
      navApproval: 'स्वीकृति',
      navPreview: 'पूर्वावलोकन',
      navEditor: 'संपादक',
      navMerchant: 'व्यापारी साइट',
      navLabs: 'लैब्स',
      
      // Main Chat / Input
      tellUsTitle: 'अपने व्यवसाय के बारे में बताएं',
      tellUsSubtitle: 'आप लिख सकते हैं, बोल सकते हैं या फोटो भेज सकते हैं। हम आपकी वेबसाइट स्वचालित रूप से बनाएंगे।',
      inputLangLabel: 'भाषा:',
      promptPlaceholder: 'अपनी भाषा में व्यवसाय की जानकारी लिखें...',
      tryExample: 'उदाहरण:',
      exampleTiffin: 'सुनीता टिफिन सर्विस',
      exampleTea: 'मेरी चाय की दुकान है',
      exampleGarage: 'मेरा कार और बाइक गैरेज है',
      exampleHandmade: 'मैं हस्तनिर्मित उत्पाद बेचता हूं',
      
      // Sample prompt texts
      sampleTiffinText: 'मेरी पुणे में सुनीता टिफिन नाम से टिफिन सेवा है। हम रोज ताजा और पौष्टिक खाना पहुंचाते हैं।',
      sampleTeaText: 'मेरी चाय की दुकान है, नाम साई टी सेंटर। हम ताजा मसाला चाय और बन मस्का परोसते हैं।',
      sampleGarageText: 'मेरा नासिक में कार और बाइक गैरेज है, नाम शिंदे ऑटो सर्विसेज। हम सर्विसिंग, ऑयल चेंज और रिपेयरिंग करते हैं।',
      sampleHandmadeText: 'मैं हस्तनिर्मित उपहार और पारंपरिक शिल्प बेचता हूं।',
      
      // Buttons & Controls
      btnSend: 'भेजें',
      btnVoice: 'आवाज इनपुट',
      btnImage: 'फोटो जोड़ें',
      btnAttach: 'फ़ाइल जोड़ें',
      btnStop: 'रोकें',
      btnRemove: 'हटाएं',
      btnReset: 'नई चैट',
      btnApprove: 'जानकारी स्वीकृत करें',
      btnSave: 'बदलाव सहेजें',
      btnBackChat: 'चैट पर वापस जाएं',
      btnBackApproval: 'जानकारी पर वापस जाएं',
      btnProceedPreview: 'वेबसाइट पूर्वावलोकन देखें',
      btnOpenEditor: 'संपादक खोलें',
      btnPublish: 'वेबसाइट प्रकाशित करें',
      btnCallNow: 'कॉल करें',
      btnAddService: '+ नई सेवा जोड़ें',
      btnUploadPhoto: 'फोटो जोड़ें',
      btnDirections: 'पता और समय',
      btnOpenSplitPreview: '👁️ पास में लाइव पूर्वावलोकन खोलें',
      previewToggleOn: 'पूर्वावलोकन: चालू',
      previewToggleOff: 'पूर्वावलोकन: बंद',
      step1Approval: 'चरण १: जानकारी अनुमोदन',
      step2Preview: 'चरण २: वेबसाइट पूर्वावलोकन',
      step3Editor: 'चरण ३: वेबसाइट संपादक',
      step4Merchant: 'चरण ४: आधिकारिक व्यापारी वेबसाइट',
      
      // Bot Messages
      botWelcome: 'नमस्ते! आपकी दुकान या व्यवसाय का क्या नाम है और आप कौन सी सेवाएं देते हैं?',
      botAck: 'धन्यवाद! मैंने आपके व्यवसाय की जानकारी दर्ज कर ली है:',
      botVoiceAck: 'आपकी आवाज प्राप्त हुई और जानकारी टेक्स्ट में बदल दी गई।',
      botImageAck: 'फोटो प्राप्त हुआ और व्यापार की जानकारी निकाल ली गई।',
      readyForApproval: 'आपकी व्यावसायिक जानकारी समीक्षा के लिए तैयार है।',
      reviewInfoBtn: 'जानकारी देखें →',
      
      // Status & Badges
      statusLiveChat: 'लाइव चैट',
      statusPending: 'स्वीकृति लंबित',
      statusApproved: 'स्वीकृत',
      statusHealthy: 'प्रणाली सक्रिय',
      statusLivePreview: 'लाइव पूर्वावलोकन',
      statusVerified: 'सत्यापित स्थानीय व्यवसाय',
      
      // Business Approval Form
      checkpoint1Title: 'व्यावसायिक जानकारी स्वीकृति',
      checkpoint1Desc: 'कृपया नीचे दी गई व्यापार जानकारी की समीक्षा करें। आवश्यकता पड़ने पर आप बदलाव कर सकते हैं।',
      approvalSuccessMsg: 'व्यावसायिक जानकारी स्वीकृत हो गई है! वेबसाइट निर्माण तैयार है।',
      labelShopName: 'दुकान का नाम',
      labelCategory: 'व्यवसाय श्रेणी',
      labelTagline: 'शीर्षक / टैगलाइन',
      labelPhone: 'फ़ोन नंबर',
      labelAddress: 'दुकान का पता',
      labelCity: 'शहर',
      labelHours: 'कामकाज के घंटे',
      labelDescription: 'व्यवसाय का विवरण',
      labelServicesTitle: 'उत्पाद और सेवाएं',
      labelServicesDesc: 'ग्राहकों के लिए उपलब्ध सभी वस्तुओं या सेवाओं की सूची।',
      labelGalleryTitle: 'दुकान की तस्वीरें',
      labelGalleryDesc: 'दुकान बोर्ड, कार्यशाला और उत्पादों की तस्वीरें।',
      labelPhoto: 'व्यवसाय फोटो / बोर्ड',
      noPhotoAttached: 'अभी कोई फोटो नहीं जुड़ा है',
      btnChangePhoto: '+ फोटो बदलें / जोड़ें',
      
      // Website Preview & Components
      checkpoint2Title: 'वेबसाइट पूर्वावलोकन',
      checkpoint2Desc: 'निर्मित वेबसाइट का निरीक्षण करें। बदलाव करने पर यहां तुरंत परिणाम दिखेगा।',
      mockNavHome: 'मुख्य',
      mockNavServices: 'सेवाएं',
      mockNavGallery: 'तस्वीरें',
      mockNavContact: 'संपर्क',
      ourServices: 'हमारी सेवाएं',
      servicesSubtitle: 'हमारी दुकान से मिलने वाली प्रमुख सेवाएं और उचित दरें।',
      galleryTitle: 'तस्वीरें',
      gallerySubtitle: 'दुकान, कार्यशाला और हमारे काम की तस्वीरें।',
      contactTitle: 'संपर्क और पता',
      contactSubtitle: 'हमारी दुकान पर आएं या सीधे फोन करें।',
      cardAddress: 'दुकान का पता',
      cardPhone: 'सीधा संपर्क',
      cardHours: 'कामकाज के घंटे',
      openMaps: 'गूगल मैप्स पर देखें ↗',
      callAvailable: 'आज कॉल के लिए उपलब्ध',
      footerRights: 'सर्वाधिकार सुरक्षित। खोजदूत प्रणाली द्वारा संचालित।',
      footerCopyright: 'सर्वाधिकार सुरक्षित। खोजदूत प्रणाली द्वारा संचालित।',
      
      // Showcase Shinde Auto Texts
      heroTitleShinde: 'नासिक में विश्वसनीय कार और बाइक सर्विस',
      heroDescShinde: 'उत्कृष्ट सेवा। उचित दरें। 15 वर्षों से स्थानीय लोगों का भरोसा।',
      svcCarTitle: 'कार सर्विस',
      svcCarDesc: 'नियमित और सामान्य सर्विसिंग, ऑयल और ब्रेक जांच',
      svcBikeTitle: 'बाइक सर्विस',
      svcBikeDesc: 'सभी टू-व्हीलर सर्विसिंग और इंजन ट्यून-अप',
      svcRepairsTitle: 'मरम्मत',
      svcRepairsDesc: 'इंजन, ब्रेक और वायरिंग मरम्मत',
      svcOilTitle: 'ऑयल परिवर्तन',
      svcOilDesc: 'सभी प्रमुख सिंथेटिक और इंजन ऑयल ब्रांड्स',
      galleryWorkshop: 'कार्यशाला और उपकरण',
      galleryDiagnostics: 'इंजन और ब्रेक जांच',
      galleryParts: 'अस्ली स्पेयर पार्ट्स',
      
      // Website Editor
      editorTitle: 'वेबसाइट संपादक',
      editorSubtitle: 'व्यापार विवरण, रंग और अनुभाग बदलें। बदलाव दाईं ओर तुरंत दिखेंगे।',
      tabContent: 'सामग्री',
      tabTheme: 'रंग और शैली',
      tabSections: 'अनुभाग',
      labelThemeColor: 'मुख्य ब्रांड रंग',
      labelFont: 'फ़ॉन्ट शैली',
      labelSectionVisibility: 'अनुभाग दिखाएं या छिपाएं',
      secHeader: 'नेविगेशन हेडर',
      secHero: 'हीरो बैनर',
      secServices: 'सेवाएं और उत्पाद',
      secGallery: 'तस्वीरें गैलरी',
      secContact: 'पता और संपर्क',
      secFooter: 'फ़ुटर',
      
      // Merchant Page
      merchantTitle: 'आधिकारिक व्यापारी वेबसाइट',
      merchantSubtitle: 'खोजदूत सत्यापित डिजिटल वेब उपस्थिति',
      selectMerchant: 'दुकान चुनें:',
      
      // Toast notifications
      toastLangChanged: 'भाषा हिंदी चुनी गई',
      toastSaved: 'बदलाव सहेजे गए',
      toastApproved: 'व्यावसायिक जानकारी स्वीकृत'
    },

    // =======================================================================
    // 100% PURE TELUGU (తెలుగు) - For Hyderabad Hackathon
    // =======================================================================
    te: {
      brandName: 'KhojDoot',
      betaBadge: 'బీటా',
      
      // Navigation
      navChat: 'చాట్',
      navApproval: 'ఆమోదం',
      navPreview: 'ప్రివ్యూ',
      navEditor: 'ఎడిటర్',
      navMerchant: 'వ్యాపారి సైట్',
      navLabs: 'ల్యాబ్స్',
      
      // Main Chat / Input
      tellUsTitle: 'మీ వ్యాపారం గురించి చెప్పండి',
      tellUsSubtitle: 'మీరు టైప్ చేయవచ్చు, మాట్లాడవచ్చు లేదా ఫోటోలు పంపవచ్చు. మేము మీ వెబ్‌సైట్‌ను స్వయంచాలకంగా సృష్టిస్తాము.',
      inputLangLabel: 'భాష:',
      promptPlaceholder: 'మీ స్వంత భాషలో వ్యాపార వివరాలను రాయండి...',
      tryExample: 'ఉదాహరణలు:',
      exampleTiffin: 'సునీత టిఫిన్ సర్వీస్',
      exampleTea: 'నాకు టీ దుకాణం ఉంది',
      exampleGarage: 'నాకు కార్ & బైక్ గ్యారేజ్ ఉంది',
      exampleHandmade: 'నేను చేతివృత్తుల వస్తువులు అమ్ముతాను',
      
      // Sample prompt texts
      sampleTiffinText: 'నాకు పూణేలో సునీత టిఫిన్ అనే టిఫిన్ సేవ ఉంది. మేము ప్రతిరోజూ తాజా ఇంటి భోజనాన్ని డెలివరీ చేస్తాము.',
      sampleTeaText: 'నాకు సాయి టీ సెంటర్ అనే టీ దుకాణం ఉంది. మేము వేడి మసాలా టీ మరియు బన్ మస్కా అందిస్తాము.',
      sampleGarageText: 'నాకు నాసిక్‌లో షిండే ఆటో సర్వీసెస్ అనే కార్ మరియు బైక్ గ్యారేజ్ ఉంది. మేము సర్వీసింగ్, ఆయిల్ మార్పు మరియు రిపేర్లు చేస్తాము.',
      sampleHandmadeText: 'నేను చేతితో తయారు చేసిన బహుమతులు మరియు సాంప్రదాయ వస్తువులు అమ్ముతాను.',
      
      // Buttons & Controls
      btnSend: 'పంపండి',
      btnVoice: 'వాయిస్ ఇన్‌పుట్',
      btnImage: 'ఫోటో జోడించండి',
      btnAttach: 'ఫైల్ జోడించండి',
      btnStop: 'ఆపు',
      btnRemove: 'తీసివేయి',
      btnReset: 'కొత్త చాట్',
      btnApprove: 'సమాచారం ఆమోదించండి',
      btnSave: 'మార్పులు సేవ్ చేయండి',
      btnBackChat: 'చాట్‌కు తిరిగి వెళ్ళు',
      btnBackApproval: 'సమాచారానికి తిరిగి వెళ్ళు',
      btnProceedPreview: 'వెబ్‌సైట్ ప్రివ్యూ చూడండి',
      btnOpenEditor: 'ఎడిటర్ తెరవండి',
      btnPublish: 'వెబ్‌సైట్ ప్రచురించండి',
      btnCallNow: 'ఇప్పుడే కాల్ చేయండి',
      btnAddService: '+ కొత్త సేవను జోడించండి',
      btnUploadPhoto: 'ఫోటో జోడించండి',
      btnDirections: 'చిరునామా & పనివేళలు',
      btnOpenSplitPreview: '👁️ చాట్ పక్కన లైవ్ ప్రివ్యూ తెరవండి',
      previewToggleOn: 'ప్రివ్యూ: ఆన్',
      previewToggleOff: 'ప్రివ్యూ: ఆఫ్',
      step1Approval: 'దశ 1: సమాచార ఆమోదం',
      step2Preview: 'దశ 2: వెబ్‌సైట్ ప్రివ్యూ',
      step3Editor: 'దశ 3: వెబ్‌సైట్ ఎడిటర్',
      step4Merchant: 'దశ 4: అధికారిక వ్యాపారి వెబ్‌సైట్',
      
      // Bot Messages
      botWelcome: 'నమస్కారం! మీ దుకాణం లేదా వ్యాపారం పేరు ఏమిటి మరియు మీరు ఏ సేవలను అందిస్తున్నారు?',
      botAck: 'ధన్యవాదాలు! నేను మీ వ్యాపార వివరాలను నమోదు చేసుకున్నాను:',
      botVoiceAck: 'మీ వాయిస్ నోట్ అందుకున్నాము మరియు విజయవంతంగా టెక్స్ట్‌గా మార్చబడింది.',
      botImageAck: 'ఫోటో అందుకున్నాము మరియు వ్యాపార వివరాలు విజయవంతంగా పొందబడ్డాయి.',
      readyForApproval: 'మీ వ్యాపార వివరాలు సమీక్ష కోసం సిద్ధంగా ఉన్నాయి.',
      reviewInfoBtn: 'వివరాలు సమీక్షించండి →',
      
      // Status & Badges
      statusLiveChat: 'లైవ్ చాట్',
      statusPending: 'ఆమోదం పెండింగ్‌లో ఉంది',
      statusApproved: 'ఆమోదించబడింది',
      statusHealthy: 'సిస్టమ్ యాక్టివ్',
      statusLivePreview: 'లైవ్ ప్రివ్యూ',
      statusVerified: 'స్థానికంగా ధృవీకరించబడిన వ్యాపారం',
      
      // Business Approval Form
      checkpoint1Title: 'వ్యాపార సమాచార ఆమోదం',
      checkpoint1Desc: 'దయచేసి దిగువ వ్యాపార వివరాలను సమీక్షించండి. అవసరమైతే మీరు ఏ రంగాన్నైనా సవరించవచ్చు.',
      approvalSuccessMsg: 'వ్యాపార సమాచారం విజయవంతంగా ఆమోదించబడింది! వెబ్‌సైట్ సృష్టికి సిద్ధంగా ఉంది.',
      labelShopName: 'దుకాణం పేరు',
      labelCategory: 'వ్యాపార వర్గం',
      labelTagline: 'శీర్షిక / ట్యాగ్‌లైన్',
      labelPhone: 'ఫోన్ నంబర్',
      labelAddress: 'దుకాణం చిరునామా',
      labelCity: 'నగరం',
      labelHours: 'పనివేళలు',
      labelDescription: 'వ్యాపార వివరణ',
      labelServicesTitle: 'ఉత్పత్తులు మరియు సేవలు',
      labelServicesDesc: 'వినియోగదారులకు అందుబాటులో ఉన్న అన్ని సేవలు మరియు ఉత్పత్తుల జాబితా.',
      labelGalleryTitle: 'దుకాణం ఫోటోలు & గ్యాలరీ',
      labelGalleryDesc: 'దుకాణం బోర్డు, పనిముట్లు మరియు ఉత్పత్తుల ఫోటోలు.',
      labelPhoto: 'వ్యాపార ఫోటో / బోర్డు',
      noPhotoAttached: 'ఇంకా ఫోటో జోడించబడలేదు',
      btnChangePhoto: '+ ఫోటో మార్చండి / జోడించండి',
      
      // Website Preview & Components
      checkpoint2Title: 'వెబ్‌సైట్ ప్రివ్యూ',
      checkpoint2Desc: 'సృష్టించబడిన వెబ్‌సైట్‌ను పరిశీలించండి. సవరించినప్పుడు ఇక్కడ వెంటనే అప్‌డేట్ అవుతుంది.',
      mockNavHome: 'హోమ్',
      mockNavServices: 'సేవలు',
      mockNavGallery: 'గ్యాలరీ',
      mockNavContact: 'సంప్రదించండి',
      ourServices: 'మా సేవలు',
      servicesSubtitle: 'మా దుకాణంలో నాణ్యమైన సేవలు మరియు సరసమైన ధరలు.',
      galleryTitle: 'ఫోటో గ్యాలరీ',
      gallerySubtitle: 'మా దుకాణం, పనిముట్లు మరియు సేవల ఫోటోలు.',
      contactTitle: 'చిరునామా & సంప్రదించండి',
      contactSubtitle: 'మా దుకాణాన్ని సందర్శించండి లేదా నేరుగా కాల్ చేయండి.',
      cardAddress: 'దుకాణం చిరునామా',
      cardPhone: 'ప్రత్యక్ష సంప్రదింపు',
      cardHours: 'పనివేళలు',
      openMaps: 'గూగుల్ మ్యాప్స్‌లో చూడండి ↗',
      callAvailable: 'ఈరోజు కాల్స్ కోసం అందుబాటులో ఉంది',
      footerRights: 'సర్వ హక్కులు ప్రత్యేకించబడ్డాయి. ఖోజ్‌దూత్ ఇంజిన్ ద్వారా ఆధారితం.',
      footerCopyright: 'సర్వ హక్కులు ప్రత్యేకించబడ్డాయి. ఖోజ్‌దూత్ ఇంజిన్ ద్వారా ఆధారితం.',
      
      // Showcase Shinde Auto Texts
      heroTitleShinde: 'నాసిక్‌లో నమ్మకమైన కార్ & బైక్ సర్వీస్',
      heroDescShinde: 'నాణ్యమైన సేవ. సరసమైన ధరలు. 15 ఏళ్లకు పైగా స్థానికుల నమ్మకం.',
      svcCarTitle: 'కార్ సర్వీస్',
      svcCarDesc: 'రెగ్యులర్ మరియు జనరల్ మెయింటెనెన్స్, ఆయిల్ & బ్రేక్ చెకప్',
      svcBikeTitle: 'బైక్ సర్వీస్',
      svcBikeDesc: 'అన్ని ద్విచక్ర వాహనాల సర్వీసింగ్ మరియు ఇంజన్ ట్యూన్-అప్',
      svcRepairsTitle: 'రిపేర్లు',
      svcRepairsDesc: 'ఇంజన్, బ్రేక్ మరియు వైరింగ్ రిపేర్లు',
      svcOilTitle: 'ఆయిల్ మార్పు',
      svcOilDesc: 'అన్ని ప్రముఖ సింథటిక్ మరియు ఇంజన్ ఆయిల్ బ్రాండ్లు',
      galleryWorkshop: 'వర్క్‌షాప్ మరియు పనిముట్లు',
      galleryDiagnostics: 'ఇంజన్ మరియు బ్రేక్ తనిఖీ',
      galleryParts: 'ఒరిజినల్ స్పేర్ పార్ట్స్',
      
      // Website Editor
      editorTitle: 'వెబ్‌సైట్ ఎడిటర్',
      editorSubtitle: 'వ్యాపార వివరాలు, రంగులు మరియు విభాగాలను మార్చండి. మార్పులు వెంటనే కనిపిస్తాయి.',
      tabContent: 'విషయ సూచిక',
      tabTheme: 'రంగులు & థీమ్',
      tabSections: 'విభాగాలు',
      labelThemeColor: 'ప్రధాన బ్రాండ్ రంగు',
      labelFont: 'ఫాంట్ శైలి',
      labelSectionVisibility: 'విభాగం చూపించు లేదా దాచు',
      secHeader: 'నావిగేషన్ హెడర్',
      secHero: 'హీరో బ్యానర్',
      secServices: 'సేవలు మరియు ఉత్పత్తులు',
      secGallery: 'ఫోటో గ్యాలరీ',
      secContact: 'చిరునామా మరియు సంప్రదింపు',
      secFooter: 'ఫుటర్',
      
      // Merchant Page
      merchantTitle: 'అధికారిక వ్యాపారి వెబ్‌సైట్',
      merchantSubtitle: 'ఖోజ్‌దూత్ ధృవీకరించిన డిజిటల్ వెబ్ ఉనికి',
      selectMerchant: 'దుకాణాన్ని ఎంచుకోండి:',
      
      // Toast notifications
      toastLangChanged: 'తెలుగు భాష ఎంపిక చేయబడింది',
      toastSaved: 'మార్పులు సేవ్ చేయబడ్డాయి',
      toastApproved: 'వ్యాపార సమాచారం ఆమోదించబడింది'
    }
  },

  init() {
    const saved = localStorage.getItem('khojdoot_lang');
    if (saved && ['en', 'mr', 'hi', 'te'].includes(saved)) {
      this.currentLanguage = saved;
    }
    this.applyTranslations();
  },

  setLanguage(langCode) {
    if (!this.translations[langCode]) return;
    this.currentLanguage = langCode;
    try {
      localStorage.setItem('khojdoot_lang', langCode);
    } catch (e) {}
    this.applyTranslations();
    window.dispatchEvent(new CustomEvent('languageChanged', { detail: { lang: langCode } }));
  },

  getLanguage() {
    return this.currentLanguage;
  },

  getLanguageName(code) {
    switch (code) {
      case 'mr': return 'मराठी';
      case 'hi': return 'हिंदी';
      case 'te': return 'తెలుగు';
      case 'en': return 'English';
      default: return code;
    }
  },

  t(key) {
    const lang = this.translations[this.currentLanguage] || this.translations.en;
    return lang[key] || this.translations.en[key] || key;
  },

  applyTranslations() {
    // 1. Text elements
    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.getAttribute('data-i18n');
      const val = this.t(key);
      if (val) {
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
          el.placeholder = val;
        } else {
          el.textContent = val;
        }
      }
    });

    // 2. Titles / Tooltips
    document.querySelectorAll('[data-i18n-title]').forEach(el => {
      const key = el.getAttribute('data-i18n-title');
      const val = this.t(key);
      if (val) el.setAttribute('title', val);
    });

    // 3. Dropdown label
    const labelEl = document.getElementById('currentLangLabel');
    if (labelEl) {
      labelEl.textContent = this.getLanguageName(this.currentLanguage);
    }

    // 4. Sync dropdown options
    document.querySelectorAll('.lang-option').forEach(opt => {
      if (opt.getAttribute('data-lang') === this.currentLanguage) {
        opt.classList.add('active');
      } else {
        opt.classList.remove('active');
      }
    });

    // 5. Update HTML lang attribute
    document.documentElement.lang = this.currentLanguage;
  }
};

document.addEventListener('DOMContentLoaded', () => {
  KhojLanguage.init();
});

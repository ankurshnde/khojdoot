/**
 * KhojDoot WebsiteSpec & Reusable Website Component System (Task 9)
 * Modular pure single-language components:
 * 1. Header / Navbar
 * 2. Hero Banner
 * 3. Products & Services Grid
 * 4. Gallery & Media Showcase
 * 5. Contact & Location Info
 * 6. Footer & Branding
 * 
 * Supports 100% pure English, Marathi, Hindi, and Telugu without mixed translations.
 */

const KhojWebsite = {
  // Sample WebsiteSpec presentation schema matching TRD Section 10
  sampleSpec: {
    version: "1.0",
    theme: {
      primaryColor: "#731c34",
      accentColor: "#1e293b",
      fontFamily: "Inter, system-ui, sans-serif",
      layoutStyle: "clean-modern"
    },
    sections: [
      { id: "header", enabled: true, showNav: true },
      { id: "hero", enabled: true, ctaText: "Call Now", showBadge: true },
      { id: "services", enabled: true, title: "Our Services", layout: "grid-4" },
      { id: "gallery", enabled: true, title: "Gallery", itemsCount: 3 },
      { id: "contact", enabled: true, title: "Contact & Location", showHours: true },
      { id: "footer", enabled: true, copyrightText: "© 2026 Powered by KhojDoot" }
    ]
  },

  getCurrentSpec() {
    try {
      const stored = localStorage.getItem('khojdoot_current_spec');
      if (stored) {
        return JSON.parse(stored);
      }
    } catch (e) {
      console.warn("Could not read localStorage", e);
    }
    return this.sampleSpec;
  },

  saveCurrentSpec(spec) {
    try {
      localStorage.setItem('khojdoot_current_spec', JSON.stringify(spec));
      window.dispatchEvent(new CustomEvent('websiteSpecUpdated', { detail: spec }));
    } catch (e) {
      console.warn("Could not write to localStorage", e);
    }
  },

  // Helper to render service icon SVGs without external dependencies
  getServiceIconSvg(iconType) {
    switch (iconType) {
      case 'wrench':
        return `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>`;
      case 'bike':
        return `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="18.5" cy="17.5" r="3.5"/><circle cx="5.5" cy="17.5" r="3.5"/><circle cx="15" cy="5" r="1"/><path d="M12 17.5V14l-3-3 4-3 2 3h2"/></svg>`;
      case 'cog':
        return `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>`;
      case 'oil':
        return `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>`;
      case 'cup':
        return `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8h1a4 4 0 0 1 0 8h-1"/><path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/><line x1="6" y1="1" x2="6" y2="4"/><line x1="10" y1="1" x2="10" y2="4"/><line x1="14" y1="1" x2="14" y2="4"/></svg>`;
      case 'bread':
      case 'food':
        return `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg>`;
      case 'grain':
      case 'spice':
        return `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/></svg>`;
      default:
        return `<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>`;
    }
  },

  // Translation helper
  t(key, fallback = '') {
    if (typeof KhojLanguage !== 'undefined' && typeof KhojLanguage.t === 'function') {
      return KhojLanguage.t(key);
    }
    return fallback;
  },

  // =========================================================================
  // Component 1: Header / Navigation Section
  // =========================================================================
  renderHeader(business, spec) {
    const tHome = this.t('mockNavHome', 'Home');
    const tServices = this.t('mockNavServices', 'Services');
    const tGallery = this.t('mockNavGallery', 'Gallery');
    const tContact = this.t('mockNavContact', 'Contact');
    const tCallNow = this.t('btnCallNow', 'Call Now');

    return `
      <header class="mock-site-nav" style="background: #ffffff; border-bottom: 1px solid #f1f5f9; padding: 16px 24px;">
        <div style="display: flex; align-items: center; gap: 8px;">
          <div style="width: 28px; height: 28px; border-radius: 6px; background-color: ${spec.theme.primaryColor}; color: #ffffff; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 13px;">
            ${(business.name || 'K').charAt(0)}
          </div>
          <div class="mock-site-brand" style="font-size: 16px; font-weight: 700; color: #111827;">${business.name}</div>
        </div>

        <div class="mock-site-links" style="display: flex; align-items: center; gap: 20px;">
          <a href="#home" class="active" style="font-size: 13px; font-weight: 500;">${tHome}</a>
          <a href="#services" style="font-size: 13px; font-weight: 500;">${tServices}</a>
          <a href="#gallery" style="font-size: 13px; font-weight: 500;">${tGallery}</a>
          <a href="#contact" style="font-size: 13px; font-weight: 500;">${tContact}</a>
          <a href="tel:${business.phone}" class="btn-brand" style="background-color: ${spec.theme.primaryColor}; font-size: 12px; padding: 6px 14px; text-decoration: none;">
            📞 ${tCallNow}
          </a>
        </div>
      </header>
    `;
  },

  // =========================================================================
  // Component 2: Hero Section
  // =========================================================================
  renderHero(business, spec) {
    const tCallNow = this.t('btnCallNow', 'Call Now');
    const tDirections = this.t('btnDirections', 'Directions & Hours');
    const tVerified = this.t('statusVerified', 'Verified Local Business');

    let heroTitle = business.tagline || business.name;
    let heroDesc = business.description || 'Quality service tailored for you.';

    if (business.id === 'shinde-auto') {
      heroTitle = this.t('heroTitleShinde', heroTitle);
      heroDesc = this.t('heroDescShinde', heroDesc);
    }

    const heroBg = (business.id === 'shinde-auto')
      ? "linear-gradient(rgba(17, 24, 39, 0.82), rgba(17, 24, 39, 0.82)), url('assets/images/garage-hero.jpg') center/cover #1e293b"
      : (business.heroImage
          ? `linear-gradient(rgba(17, 24, 39, 0.82), rgba(17, 24, 39, 0.82)), url('${business.heroImage}') center/cover #1e293b`
          : `linear-gradient(135deg, ${spec.theme.primaryColor || '#731c34'} 0%, #1e293b 100%)`);

    return `
      <section id="home" class="mock-hero" style="background: ${heroBg}; color: #ffffff; padding: 56px 28px; text-align: left;">
        <div style="max-width: 600px;">
          <div style="display: inline-flex; align-items: center; gap: 6px; background: rgba(255, 255, 255, 0.15); backdrop-filter: blur(4px); padding: 4px 12px; border-radius: 9999px; font-size: 12px; font-weight: 600; margin-bottom: 16px;">
            <span>✓</span> ${tVerified}
          </div>
          <h2 style="font-size: 28px; font-weight: 800; line-height: 1.25; margin-bottom: 12px; color: #ffffff;">
            ${heroTitle}
          </h2>
          <p style="font-size: 14px; line-height: 1.6; color: #e2e8f0; margin-bottom: 24px;">
            ${heroDesc}
          </p>
          <div style="display: flex; gap: 12px; flex-wrap: wrap;">
            <a href="tel:${business.phone}" class="btn-brand" style="background-color: ${spec.theme.primaryColor}; padding: 10px 22px; font-size: 14px; text-decoration: none; border-radius: 6px;">
              📞 ${tCallNow} (${business.phone})
            </a>
            <a href="#contact" class="btn btn-outline" style="background: rgba(255,255,255,0.1); border-color: rgba(255,255,255,0.3); color: #ffffff; padding: 10px 18px; font-size: 14px; text-decoration: none; border-radius: 6px;">
              📍 ${tDirections}
            </a>
          </div>
        </div>
      </section>
    `;
  },

  // =========================================================================
  // Component 3: Products or Services Section
  // =========================================================================
  renderServices(business, spec) {
    const tOurServices = this.t('ourServices', 'Our Services');
    const tServicesSub = this.t('servicesSubtitle', 'Quality services offered at fair prices.');
    const services = business.services || [];

    const isShinde = (business.id === 'shinde-auto');

    const cardsHtml = services.map((svc, idx) => {
      let title = svc.name;
      let desc = svc.description;

      if (isShinde) {
        if (idx === 0) { title = this.t('svcCarTitle', title); desc = this.t('svcCarDesc', desc); }
        else if (idx === 1) { title = this.t('svcBikeTitle', title); desc = this.t('svcBikeDesc', desc); }
        else if (idx === 2) { title = this.t('svcRepairsTitle', title); desc = this.t('svcRepairsDesc', desc); }
        else if (idx === 3) { title = this.t('svcOilTitle', title); desc = this.t('svcOilDesc', desc); }
      }

      return `
        <div class="service-card" style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px 16px; text-align: left; box-shadow: 0 1px 3px rgba(0,0,0,0.05); transition: transform 0.2s;">
          <div style="width: 40px; height: 40px; border-radius: 8px; background: #fdf2f4; color: ${spec.theme.primaryColor}; display: flex; align-items: center; justify-content: center; margin-bottom: 12px;">
            ${this.getServiceIconSvg(svc.icon)}
          </div>
          <div class="service-card-title" style="font-size: 15px; font-weight: 700; color: #111827; margin-bottom: 4px;">
            ${title}
          </div>
          <div class="service-card-desc" style="font-size: 12px; color: #64748b; line-height: 1.5; margin-bottom: 12px;">
            ${desc}
          </div>
          <div style="font-size: 13px; font-weight: 700; color: ${spec.theme.primaryColor}; background: #f8fafc; padding: 4px 8px; border-radius: 4px; display: inline-block;">
            ${svc.price || ''}
          </div>
        </div>
      `;
    }).join('');

    return `
      <section id="services" style="padding: 44px 28px; background: #f8fafc;">
        <div style="text-align: center; max-width: 600px; margin: 0 auto 32px;">
          <h3 style="font-size: 22px; font-weight: 700; color: #111827; margin-bottom: 6px;">
            ${tOurServices}
          </h3>
          <p style="font-size: 13px; color: #64748b;">
            ${tServicesSub}
          </p>
        </div>
        <div class="services-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px;">
          ${cardsHtml}
        </div>
      </section>
    `;
  },

  // =========================================================================
  // Component 4: Gallery Section
  // =========================================================================
  renderGallery(business, spec) {
    const tGalleryTitle = this.t('galleryTitle', 'Photo Gallery');
    const tGallerySub = this.t('gallerySubtitle', 'Glimpses of our store, equipment, and recent work.');
    const isShinde = (business.id === 'shinde-auto');

    const defaultGallery = [
      { title: isShinde ? this.t('galleryWorkshop', 'Workshop & Tools') : 'Store', url: "assets/images/service1.jpg" },
      { title: isShinde ? this.t('galleryDiagnostics', 'Diagnostics & Inspection') : 'Equipment', url: "assets/images/service2.jpg" },
      { title: isShinde ? this.t('galleryParts', 'Genuine Spare Parts') : 'Products', url: "assets/images/service3.jpg" }
    ];

    const gallery = (business.gallery && business.gallery.length > 0) ? business.gallery : defaultGallery;

    const galleryCards = gallery.map((item, idx) => {
      let title = item.title;
      if (isShinde) {
        if (idx === 0) title = this.t('galleryWorkshop', title);
        else if (idx === 1) title = this.t('galleryDiagnostics', title);
        else if (idx === 2) title = this.t('galleryParts', title);
      }

      return `
        <div style="position: relative; border-radius: 8px; overflow: hidden; background: #1e293b; aspect-ratio: 4 / 3; display: flex; align-items: flex-end;">
          <img src="${item.url}" alt="${title}" style="width: 100%; height: 100%; object-fit: cover; position: absolute; top:0; left:0;" onerror="this.src='https://placehold.co/400x300/1e293b/ffffff?text=Gallery+${idx+1}'">
          <div style="position: relative; z-index: 2; width: 100%; background: linear-gradient(transparent, rgba(15, 23, 42, 0.9)); padding: 12px 14px; color: #ffffff; font-size: 12px; font-weight: 600;">
            ${title}
          </div>
        </div>
      `;
    }).join('');

    return `
      <section id="gallery" style="padding: 44px 28px; background: #ffffff;">
        <div style="text-align: center; max-width: 600px; margin: 0 auto 32px;">
          <h3 style="font-size: 22px; font-weight: 700; color: #111827; margin-bottom: 6px;">
            ${tGalleryTitle}
          </h3>
          <p style="font-size: 13px; color: #64748b;">
            ${tGallerySub}
          </p>
        </div>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px;">
          ${galleryCards}
        </div>
      </section>
    `;
  },

  // =========================================================================
  // Component 5: Contact & Location Section
  // =========================================================================
  renderContact(business, spec) {
    const tContactTitle = this.t('contactTitle', 'Contact & Location');
    const tContactSub = this.t('contactSubtitle', 'Visit our store or call us directly.');
    const tCardAddress = this.t('cardAddress', 'Store Address');
    const tCardPhone = this.t('cardPhone', 'Direct Call');
    const tCardHours = this.t('cardHours', 'Working Hours');
    const tOpenMaps = this.t('openMaps', 'Open in Google Maps ↗');
    const tCallAvailable = this.t('callAvailable', 'Open for calls today');
    const tCategory = this.t('labelCategory', 'Category');

    return `
      <section id="contact" style="padding: 44px 28px; background: #f8fafc; border-top: 1px solid #f1f5f9;">
        <div style="text-align: center; max-width: 600px; margin: 0 auto 32px;">
          <h3 style="font-size: 22px; font-weight: 700; color: #111827; margin-bottom: 6px;">
            ${tContactTitle}
          </h3>
          <p style="font-size: 13px; color: #64748b;">
            ${tContactSub}
          </p>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 20px;">
          <!-- Card 1: Address -->
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px;">
            <div style="font-size: 24px; margin-bottom: 8px;">📍</div>
            <h4 style="font-size: 15px; font-weight: 700; color: #111827; margin-bottom: 6px;">${tCardAddress}</h4>
            <p style="font-size: 13px; color: #475569; line-height: 1.5; margin-bottom: 12px;">
              ${business.address || ''}<br>
              <strong>${business.city || ''}</strong>
            </p>
            <a href="https://maps.google.com/?q=${encodeURIComponent(business.name + ' ' + business.city)}" target="_blank" style="font-size: 12px; font-weight: 600; color: ${spec.theme.primaryColor}; text-decoration: none;">
              ${tOpenMaps}
            </a>
          </div>

          <!-- Card 2: Contact Numbers -->
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px;">
            <div style="font-size: 24px; margin-bottom: 8px;">📞</div>
            <h4 style="font-size: 15px; font-weight: 700; color: #111827; margin-bottom: 6px;">${tCardPhone}</h4>
            <p style="font-size: 13px; color: #475569; line-height: 1.5; margin-bottom: 12px;">
              ${tContactSub}
            </p>
            <a href="tel:${business.phone}" style="display: inline-block; font-size: 16px; font-weight: 700; color: ${spec.theme.primaryColor}; text-decoration: none; margin-bottom: 8px;">
              ${business.phone}
            </a>
            <div style="font-size: 11px; color: #16a34a; font-weight: 500;">● ${tCallAvailable}</div>
          </div>

          <!-- Card 3: Working Hours -->
          <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 20px;">
            <div style="font-size: 24px; margin-bottom: 8px;">⏰</div>
            <h4 style="font-size: 15px; font-weight: 700; color: #111827; margin-bottom: 6px;">${tCardHours}</h4>
            <p style="font-size: 13px; color: #475569; line-height: 1.5; margin-bottom: 8px;">
              ${business.hours || ''}
            </p>
            <div style="font-size: 12px; color: #64748b;">
              ${tCategory}: <strong>${business.category || 'General'}</strong>
            </div>
          </div>
        </div>
      </section>
    `;
  },

  // =========================================================================
  // Component 6: Footer Section
  // =========================================================================
  renderFooter(business, spec) {
    const tHome = this.t('mockNavHome', 'Home');
    const tServices = this.t('mockNavServices', 'Services');
    const tGallery = this.t('mockNavGallery', 'Gallery');
    const tContact = this.t('mockNavContact', 'Contact');
    const tRights = this.t('footerRights', 'All rights reserved. Powered by KhojDoot.');

    return `
      <footer style="background: #111827; color: #94a3b8; padding: 36px 28px 24px; text-align: center; border-top: 1px solid #1f2937;">
        <div style="max-width: 600px; margin: 0 auto;">
          <div style="font-size: 18px; font-weight: 700; color: #ffffff; margin-bottom: 6px;">
            ${business.name}
          </div>
          <p style="font-size: 13px; color: #9ca3af; margin-bottom: 16px;">
            ${business.tagline || business.description || ''}
          </p>
          <div style="display: flex; justify-content: center; gap: 16px; font-size: 12px; margin-bottom: 20px;">
            <a href="#home" style="color: #cbd5e1; text-decoration: none;">${tHome}</a>
            <a href="#services" style="color: #cbd5e1; text-decoration: none;">${tServices}</a>
            <a href="#gallery" style="color: #cbd5e1; text-decoration: none;">${tGallery}</a>
            <a href="#contact" style="color: #cbd5e1; text-decoration: none;">${tContact}</a>
          </div>
          <div style="font-size: 11px; color: #6b7280; border-top: 1px solid #1f2937; padding-top: 16px;">
            © 2026 ${business.name}. ${tRights}
          </div>
        </div>
      </footer>
    `;
  },

  // Helper to check if section is enabled in WebsiteSpec
  isSectionEnabled(spec, sectionId) {
    if (!spec || !spec.sections) return true;
    const sec = spec.sections.find(s => s.id === sectionId);
    return sec ? (sec.enabled !== false) : true;
  },

  // =========================================================================
  // Combined Master Component Renderer
  // =========================================================================
  renderCompleteWebsite(business, spec) {
    business = business || KhojBusiness.getCurrentBusiness();
    spec = spec || this.getCurrentSpec();

    const headerHtml = this.isSectionEnabled(spec, 'header') ? this.renderHeader(business, spec) : '';
    const heroHtml = this.isSectionEnabled(spec, 'hero') ? this.renderHero(business, spec) : '';
    const servicesHtml = this.isSectionEnabled(spec, 'services') ? this.renderServices(business, spec) : '';
    const galleryHtml = this.isSectionEnabled(spec, 'gallery') ? this.renderGallery(business, spec) : '';
    const contactHtml = this.isSectionEnabled(spec, 'contact') ? this.renderContact(business, spec) : '';
    const footerHtml = this.isSectionEnabled(spec, 'footer') ? this.renderFooter(business, spec) : '';

    return `
      <div class="rendered-merchant-site" style="font-family: ${spec.theme.fontFamily || 'inherit'};">
        ${headerHtml}
        ${heroHtml}
        ${servicesHtml}
        ${galleryHtml}
        ${contactHtml}
        ${footerHtml}
      </div>
    `;
  },

  // Backward-compatible preview html caller
  renderPreviewHtml(business, spec) {
    return this.renderCompleteWebsite(business, spec);
  },

  // Conversational and Voice Editing Engine
  applyConversationalEdit(instruction, business, spec) {
    if (!instruction) return { business, spec, changes: [] };
    business = business || KhojBusiness.getCurrentBusiness();
    spec = spec || this.getCurrentSpec();
    const text = instruction.toLowerCase().trim();
    const changes = [];

    // 1. Color / Theme edits
    if (text.includes('saffron') || text.includes('bhagwa') || text.includes('भगवा') || text.includes('केसरी') || text.includes('orange') || text.includes('नारंगी')) {
      spec.theme.primaryColor = '#f0a000';
      spec.theme.layoutStyle = 'traditional';
      changes.push('थीम रंग बदलला: भगवा (Saffron)');
    } else if (text.includes('blue') || text.includes('निळा') || text.includes('नीला') || text.includes('modern') || text.includes('आधुनिक')) {
      spec.theme.primaryColor = '#2563eb';
      spec.theme.layoutStyle = 'clean-modern';
      changes.push('थीम रंग बदलला: आधुनिक निळा (Blue)');
    } else if (text.includes('green') || text.includes('हिरवा') || text.includes('हरा')) {
      spec.theme.primaryColor = '#16a34a';
      changes.push('थीम रंग बदलला: हिरवा (Green)');
    } else if (text.includes('maroon') || text.includes('लाल') || text.includes('तांबडा') || text.includes('red')) {
      spec.theme.primaryColor = '#731c34';
      changes.push('थीम रंग बदलला: मरून (Maroon)');
    } else if (text.includes('dark') || text.includes('black') || text.includes('काळा')) {
      spec.theme.primaryColor = '#1e293b';
      changes.push('थीम रंग बदलला: डार्क (Slate Dark)');
    }

    // 2. Section toggles
    if (text.includes('gallery hide') || text.includes('गॅलरी लपवा') || text.includes('गॅलरी बंद') || text.includes('hide gallery') || text.includes('remove gallery')) {
      const s = spec.sections.find(x => x.id === 'gallery');
      if (s) s.enabled = false;
      changes.push('गॅलरी विभाग लपवला (Gallery Hidden)');
    } else if (text.includes('gallery show') || text.includes('गॅलरी दाखवा') || text.includes('गॅलरी चालू') || text.includes('show gallery')) {
      const s = spec.sections.find(x => x.id === 'gallery');
      if (s) s.enabled = true;
      changes.push('गॅलरी विभाग दाखवला (Gallery Enabled)');
    }

    // 3. Add or update service
    const addSvcMatch = text.match(/(?:add service|सेवा जोडा|service add)\s+([^\d\,\.\n]+?)(?:\s+(?:for|at|रु|₹|rs)?\s*(\d+))?$/i) ||
                        text.match(/(?:नवीन सेवा|new service)\s+([^\d\,\.\n]+?)(?:\s+(?:for|at|रु|₹|rs)?\s*(\d+))?$/i);
    if (addSvcMatch) {
      const svcName = addSvcMatch[1].trim();
      const svcPrice = addSvcMatch[2] ? `₹${addSvcMatch[2]}` : 'योग्य दरात';
      if (!business.services) business.services = [];
      business.services.push({
        name: svcName,
        description: 'ग्राहकांसाठी विशेष सेवा',
        price: svcPrice,
        icon: 'wrench'
      });
      changes.push(`नवीन सेवा जोडली: ${svcName} (${svcPrice})`);
    }

    // 4. Update hours
    const hoursMatch = text.match(/(?:hours|वेळा|time|timing)\s+(.+)/i);
    if (hoursMatch) {
      business.hours = hoursMatch[1].trim();
      changes.push(`कामाच्या वेळा बदलल्या: ${business.hours}`);
    }

    // 5. Update phone
    const phoneMatch = text.match(/(?:phone|mobile|नंबर|मोबाईल)\s+(\+?\d[\d\s-]{8,14}\d)/i);
    if (phoneMatch) {
      business.phone = phoneMatch[1].replace(/\s+/g, '');
      changes.push(`फोन नंबर अपडेट केला: ${business.phone}`);
    }

    if (changes.length === 0) {
      business.tagline = instruction.trim();
      changes.push(`टॅगलाइन/वर्णन अपडेट केले: "${instruction}"`);
    }

    this.saveCurrentSpec(spec);
    if (typeof KhojBusiness !== 'undefined') {
      KhojBusiness.saveCurrentBusiness(business);
    }
    return { business, spec, changes };
  }
};

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Surse Law Firm | Premier Legal Services in India</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="Surse Law Firm - Professional legal services across Corporate, Family, Property and Litigation matters in India. Bar Council of India compliant.">
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    /* ===== CSS VARIABLES ===== */
    :root {
      --bg-dark: #0a0a12;
      --bg-navy: #0d1021;
      --bg-card: rgba(255, 255, 255, 0.03);
      --primary: #ffffff;
      --secondary: #9ca3af;
      --text-desc: #b8c5d6;

      /* Premium Colorful Palette */
      --gold: #f0c14b;
      --gold-light: #ffd966;
      --gold-dark: #c9a227;
      --purple: #a855f7;
      --purple-dark: #7c3aed;
      --teal: #14b8a6;
      --teal-dark: #0d9488;
      --blue: #3b82f6;
      --blue-light: #60a5fa;
      --rose: #f43f5e;
      --orange: #f97316;
      --emerald: #10b981;
      --cyan: #06b6d4;
      --pink: #ec4899;
      
      /* Gradients */
      --gradient-gold: linear-gradient(135deg, #f0c14b 0%, #ffd966 50%, #c9a227 100%);
      --gradient-purple: linear-gradient(135deg, #a855f7, #7c3aed);
      --gradient-teal: linear-gradient(135deg, #14b8a6, #0d9488);
      --gradient-blue: linear-gradient(135deg, #3b82f6, #1d4ed8);
      --gradient-rose: linear-gradient(135deg, #f43f5e, #e11d48);
      --gradient-rainbow: linear-gradient(90deg, #f0c14b, #a855f7, #14b8a6, #3b82f6, #f43f5e);
      --gradient-premium: linear-gradient(135deg, #1a1a2e, #16213e, #0f3460);
      
      --border: rgba(240, 193, 75, 0.2);
      --border-purple: rgba(168, 85, 247, 0.3);
      --glow-gold: 0 0 40px rgba(240, 193, 75, 0.4);
      --glow-purple: 0 0 40px rgba(168, 85, 247, 0.4);
      --glow-teal: 0 0 40px rgba(20, 184, 166, 0.4);
      
      --transition: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
      --transition-bounce: 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
      --transition-elastic: 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    /* ===== RESET ===== */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
    }

    ::-webkit-scrollbar { width: 10px; }
    ::-webkit-scrollbar-track { background: var(--bg-dark); }
    ::-webkit-scrollbar-thumb {
      background: var(--gradient-rainbow);
      border-radius: 5px;
    }

    body {
      font-family: 'Montserrat', sans-serif;
      background: var(--bg-dark);
      color: var(--primary);
      line-height: 1.6;
      overflow-x: hidden;
    }

    /* ===== PRELOADER ===== */
    .preloader {
      position: fixed;
      inset: 0;
      background: linear-gradient(135deg, #0a0a12, #1a1a2e);
      z-index: 99999;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-direction: column;
      gap: 30px;
    }
    .preloader.hide {
      animation: preloaderHide 1s ease forwards;
    }
    @keyframes preloaderHide {
      0% { opacity: 1; }
      100% { opacity: 0; visibility: hidden; pointer-events: none; }
    }

    .preloader-icon {
      width: 120px;
      height: 120px;
      position: relative;
    }
    .preloader-icon::before {
      content: '⚖️';
      font-size: 80px;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
      animation: scaleRotate 2s ease-in-out infinite;
    }
    @keyframes scaleRotate {
      0%, 100% { transform: translate(-50%, -50%) scale(1) rotate(-10deg); }
      50% { transform: translate(-50%, -50%) scale(1.2) rotate(10deg); }
    }

    .preloader-ring {
      position: absolute;
      inset: -10px;
      border: 4px solid transparent;
      border-top-color: var(--gold);
      border-right-color: var(--purple);
      border-radius: 50%;
      animation: ringRotate 1.5s linear infinite;
    }
    @keyframes ringRotate {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }

    .preloader-logo {
      font-family: 'Cormorant Garamond', serif;
      font-size: 52px;
      font-weight: 700;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 3s ease-in-out infinite;
      text-align: center;
    }
    @keyframes rainbowShift {
      0%, 100% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
    }
    .preloader-tagline {
      font-size: 12px;
      letter-spacing: 6px;
      text-transform: uppercase;
      background: linear-gradient(90deg, var(--gold), var(--teal), var(--purple));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }
    .preloader-bar {
      width: 250px;
      height: 4px;
      background: rgba(255,255,255,0.1);
      border-radius: 4px;
      overflow: hidden;
    }
    .preloader-bar::after {
      content: '';
      display: block;
      width: 100%;
      height: 100%;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      animation: loadingBar 1.5s ease-in-out infinite, rainbowShift 2s ease-in-out infinite;
    }
    @keyframes loadingBar {
      0% { transform: translateX(-100%); }
      100% { transform: translateX(100%); }
    }

    /* ===== BACKGROUND EFFECTS ===== */
    .bg-effects {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    .gradient-orbs {
      position: absolute;
      inset: 0;
    }
    .orb {
      position: absolute;
      border-radius: 50%;
      filter: blur(80px);
      opacity: 0.6;
      animation: orbFloat 20s ease-in-out infinite;
    }
    .orb-gold {
      width: 500px;
      height: 500px;
      background: radial-gradient(circle, var(--gold), transparent 70%);
      top: -10%;
      left: -10%;
    }
    .orb-purple {
      width: 400px;
      height: 400px;
      background: radial-gradient(circle, var(--purple), transparent 70%);
      top: 40%;
      right: -5%;
      animation-delay: -7s;
    }
    .orb-teal {
      width: 450px;
      height: 450px;
      background: radial-gradient(circle, var(--teal), transparent 70%);
      bottom: -10%;
      left: 30%;
      animation-delay: -14s;
    }
    .orb-rose {
      width: 350px;
      height: 350px;
      background: radial-gradient(circle, var(--rose), transparent 70%);
      top: 60%;
      left: 10%;
      animation-delay: -10s;
    }

    @keyframes orbFloat {
      0%, 100% { transform: translate(0, 0) scale(1); }
      25% { transform: translate(50px, -30px) scale(1.1); }
      50% { transform: translate(-30px, 50px) scale(0.9); }
      75% { transform: translate(30px, 30px) scale(1.05); }
    }

    .grid-pattern {
      position: absolute;
      inset: 0;
      background-image: 
        linear-gradient(rgba(240,193,75,0.03) 1px, transparent 1px),
        linear-gradient(90deg, rgba(240,193,75,0.03) 1px, transparent 1px);
      background-size: 60px 60px;
      mask-image: radial-gradient(ellipse at center, black 0%, transparent 75%);
    }

    .floating-icons {
      position: absolute;
      inset: 0;
    }
    .float-icon {
      position: absolute;
      font-size: 30px;
      opacity: 0.15;
      animation: floatIcon 15s ease-in-out infinite;
    }
    .float-icon:nth-child(1) { top: 15%; left: 8%; animation-delay: 0s; }
    .float-icon:nth-child(2) { top: 70%; left: 85%; animation-delay: -3s; }
    .float-icon:nth-child(3) { top: 85%; left: 20%; animation-delay: -6s; }
    .float-icon:nth-child(4) { top: 25%; right: 12%; animation-delay: -9s; }
    .float-icon:nth-child(5) { top: 50%; left: 5%; animation-delay: -12s; }

    @keyframes floatIcon {
      0%, 100% { transform: translateY(0) rotate(0deg); opacity: 0.15; }
      50% { transform: translateY(-40px) rotate(15deg); opacity: 0.25; }
    }

    /* ===== DISCLAIMER POPUP ===== */
    .disclaimer-overlay {
      position: fixed;
      inset: 0;
      background: rgba(0, 0, 0, 0.95);
      backdrop-filter: blur(25px);
      z-index: 100000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 20px;
      opacity: 0;
      visibility: hidden;
      transition: var(--transition);
    }
    .disclaimer-overlay.active {
      opacity: 1;
      visibility: visible;
    }
    .disclaimer-modal {
      background: linear-gradient(145deg, #151520, #0d0d15);
      border: 2px solid;
      border-image: var(--gradient-rainbow) 1;
      border-radius: 30px;
      max-width: 650px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 50px;
      position: relative;
      transform: scale(0.8) translateY(50px);
      transition: var(--transition-elastic);
      box-shadow: 0 0 60px rgba(240,193,75,0.2), 0 0 100px rgba(168,85,247,0.1);
    }
    .disclaimer-overlay.active .disclaimer-modal {
      transform: scale(1) translateY(0);
    }
    .disclaimer-header {
      text-align: center;
      margin-bottom: 30px;
    }
    .disclaimer-icon {
      width: 100px;
      height: 100px;
      margin: 0 auto 20px;
      background: var(--gradient-gold);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 50px;
      box-shadow: var(--glow-gold);
    }
    .disclaimer-header h2 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 36px;
      font-weight: 700;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 3s ease-in-out infinite;
      margin-bottom: 10px;
    }
    .disclaimer-header p {
      color: var(--text-desc);
      font-size: 14px;
    }
    .disclaimer-content {
      background: rgba(240, 193, 75, 0.05);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 25px;
      margin-bottom: 30px;
    }
    .disclaimer-content h3 {
      color: var(--gold);
      font-size: 16px;
      margin-bottom: 15px;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .disclaimer-content p {
      font-size: 14px;
      color: var(--text-desc);
      margin-bottom: 12px;
      line-height: 1.7;
    }
    .disclaimer-content p:last-child { margin-bottom: 0; }
    .disclaimer-content strong { color: var(--primary); }
    .disclaimer-list {
      list-style: none;
      margin: 15px 0;
    }
    .disclaimer-list li {
      font-size: 13px;
      color: var(--text-desc);
      padding: 10px 0;
      padding-left: 30px;
      position: relative;
      border-bottom: 1px solid rgba(240,193,75,0.1);
    }
    .disclaimer-list li::before {
      content: '⚖️';
      position: absolute;
      left: 0;
      font-size: 14px;
    }
    .disclaimer-checkbox {
      display: flex;
      align-items: flex-start;
      gap: 15px;
      margin-bottom: 25px;
      padding: 20px;
      background: linear-gradient(135deg, rgba(168,85,247,0.1), rgba(20,184,166,0.1));
      border-radius: 12px;
      cursor: pointer;
      border: 1px solid var(--border-purple);
      transition: var(--transition);
    }
    .disclaimer-checkbox:hover {
      border-color: var(--purple);
    }
    .disclaimer-checkbox input {
      width: 24px;
      height: 24px;
      accent-color: var(--purple);
      cursor: pointer;
      flex-shrink: 0;
      margin-top: 2px;
    }
    .disclaimer-checkbox label {
      font-size: 14px;
      color: var(--primary);
      cursor: pointer;
    }
    .disclaimer-buttons {
      display: flex;
      gap: 15px;
    }
    .disclaimer-buttons button {
      flex: 1;
      padding: 18px 30px;
      border-radius: 100px;
      font-size: 15px;
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition-bounce);
      border: none;
      font-family: inherit;
    }
    .btn-exit {
      background: rgba(255,255,255,0.05);
      color: var(--secondary);
      border: 1px solid rgba(255,255,255,0.1);
    }
    .btn-exit:hover {
      background: var(--gradient-rose);
      color: white;
      border-color: transparent;
    }
    .btn-agree {
      background: var(--gradient-purple);
      color: white;
      box-shadow: var(--glow-purple);
    }
    .btn-agree:hover {
      transform: translateY(-3px) scale(1.02);
      box-shadow: 0 0 50px rgba(168,85,247,0.6);
    }
    .btn-agree:disabled {
      opacity: 0.5;
      cursor: not-allowed;
      transform: none;
    }

    /* ===== NAVIGATION ===== */
    .nav-wrapper {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 1000;
      padding: 20px 40px;
      transition: var(--transition);
    }
    .nav-wrapper.scrolled {
      padding: 12px 40px;
    }
    .nav-container {
      max-width: 1400px;
      margin: 0 auto;
      background: rgba(10, 10, 18, 0.85);
      backdrop-filter: blur(20px);
      border: 1px solid var(--border);
      border-radius: 100px;
      padding: 12px 30px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      transition: var(--transition);
    }
    .nav-wrapper.scrolled .nav-container {
      background: rgba(10, 10, 18, 0.95);
      box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5), 0 0 30px rgba(240, 193, 75, 0.1);
    }
    .logo {
      display: flex;
      align-items: center;
      gap: 15px;
      text-decoration: none;
    }
    .logo-icon {
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: var(--gradient-gold);
      display: flex;
      align-items: center;
      justify-content: center;
      font-family: 'Cormorant Garamond', serif;
      font-size: 24px;
      font-weight: 700;
      color: #0a0a12;
      transition: var(--transition-bounce);
      box-shadow: 0 5px 20px rgba(240, 193, 75, 0.3);
    }
    .logo:hover .logo-icon {
      transform: rotate(-10deg) scale(1.1);
      box-shadow: var(--glow-gold);
    }
    .logo-text {
      font-family: 'Cormorant Garamond', serif;
      font-weight: 700;
      font-size: 22px;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 5s ease-in-out infinite;
    }
    .nav-links {
      display: flex;
      align-items: center;
      gap: 8px;
      list-style: none;
    }
    .nav-links a {
      text-decoration: none;
      color: var(--secondary);
      font-size: 14px;
      font-weight: 500;
      padding: 12px 22px;
      border-radius: 50px;
      transition: var(--transition);
      position: relative;
    }
    .nav-links a::after {
      content: '';
      position: absolute;
      bottom: 8px;
      left: 50%;
      width: 0;
      height: 2px;
      background: var(--gradient-rainbow);
      transition: var(--transition);
      transform: translateX(-50%);
    }
    .nav-links a:hover {
      color: var(--gold);
    }
    .nav-links a:hover::after {
      width: 30px;
    }
    .nav-cta {
      background: var(--gradient-purple) !important;
      color: white !important;
      font-weight: 600 !important;
      box-shadow: 0 5px 20px rgba(168, 85, 247, 0.3);
    }
    .nav-cta::after { display: none !important; }
    .nav-cta:hover {
      transform: translateY(-3px) scale(1.02) !important;
      box-shadow: var(--glow-purple) !important;
    }

    .menu-btn {
      display: none;
      width: 50px;
      height: 50px;
      border-radius: 50%;
      background: var(--gradient-purple);
      border: none;
      cursor: pointer;
      position: relative;
      transition: var(--transition);
    }
    .menu-btn:hover { transform: scale(1.1); }
    .menu-btn span {
      position: absolute;
      left: 50%;
      width: 22px;
      height: 2px;
      background: white;
      border-radius: 2px;
      transform: translateX(-50%);
      transition: var(--transition);
    }
    .menu-btn span:nth-child(1) { top: 17px; }
    .menu-btn span:nth-child(2) { top: 24px; }
    .menu-btn span:nth-child(3) { top: 31px; }
    .menu-btn.active span:nth-child(1) { top: 24px; transform: translateX(-50%) rotate(45deg); }
    .menu-btn.active span:nth-child(2) { opacity: 0; }
    .menu-btn.active span:nth-child(3) { top: 24px; transform: translateX(-50%) rotate(-45deg); }

    .mobile-nav {
      position: fixed;
      inset: 0;
      background: rgba(10, 10, 18, 0.98);
      backdrop-filter: blur(20px);
      z-index: 999;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      gap: 25px;
      opacity: 0;
      visibility: hidden;
      transition: var(--transition);
    }
    .mobile-nav.active { opacity: 1; visibility: visible; }
    .mobile-nav a {
      text-decoration: none;
      font-family: 'Cormorant Garamond', serif;
      font-size: 32px;
      font-weight: 600;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 3s ease-in-out infinite;
      opacity: 0;
      transform: translateY(30px);
      transition: var(--transition-elastic);
    }
    .mobile-nav.active a { opacity: 1; transform: translateY(0); }
    .mobile-nav a:nth-child(1) { transition-delay: 0.1s; }
    .mobile-nav a:nth-child(2) { transition-delay: 0.15s; }
    .mobile-nav a:nth-child(3) { transition-delay: 0.2s; }
    .mobile-nav a:nth-child(4) { transition-delay: 0.25s; }
    .mobile-nav a:nth-child(5) { transition-delay: 0.3s; }
    .mobile-nav a:nth-child(6) { transition-delay: 0.35s; }
    .mobile-nav a:hover { transform: scale(1.1); }

    /* ===== HERO SECTION ===== */
    .hero {
      min-height: 100vh;
      display: flex;
      align-items: center;
      padding: 140px 40px 100px;
      position: relative;
      overflow: hidden;
    }
    .hero-container {
      max-width: 1400px;
      margin: 0 auto;
      width: 100%;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 80px;
      align-items: center;
    }
    .hero-content {
      position: relative;
      z-index: 2;
    }
    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      background: linear-gradient(135deg, rgba(240,193,75,0.15), rgba(168,85,247,0.15));
      border: 1px solid var(--border);
      padding: 12px 28px;
      border-radius: 100px;
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 30px;
      animation: fadeSlideUp 1s ease 0.3s both;
    }
    @keyframes fadeSlideUp {
      from { opacity: 0; transform: translateY(30px); }
      to { opacity: 1; transform: translateY(0); }
    }
    .hero-badge .pulse-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--emerald);
      animation: pulse 2s ease-in-out infinite;
      box-shadow: 0 0 10px var(--emerald);
    }
    @keyframes pulse {
      0%, 100% { transform: scale(1); opacity: 1; }
      50% { transform: scale(1.3); opacity: 0.7; }
    }
    .hero-badge span {
      background: linear-gradient(90deg, var(--gold), var(--teal), var(--purple));
      background-size: 200% 200%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 3s ease-in-out infinite;
    }

    .hero-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(48px, 7vw, 85px);
      font-weight: 700;
      line-height: 1.1;
      letter-spacing: -2px;
      margin-bottom: 30px;
    }
    .hero-title .line {
      display: block;
      overflow: hidden;
    }
    .hero-title .line span {
      display: inline-block;
      animation: titleReveal 1s var(--transition-elastic) both;
    }
    .hero-title .line:nth-child(1) span { animation-delay: 0.5s; }
    .hero-title .line:nth-child(2) span { animation-delay: 0.7s; }
    .hero-title .line:nth-child(3) span { animation-delay: 0.9s; }
    @keyframes titleReveal {
      from { transform: translateY(100%); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }
    .hero-title .gradient-text {
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 4s ease-in-out infinite;
    }

    /* Premium Colorful Subtitle */
    .hero-subtitle {
      font-size: 18px;
      max-width: 600px;
      line-height: 2;
      margin-bottom: 40px;
      animation: fadeSlideUp 1s ease 1.1s both;
      position: relative;
      padding: 25px 30px;
      background: linear-gradient(135deg, rgba(240,193,75,0.08), rgba(168,85,247,0.08), rgba(20,184,166,0.08));
      border-radius: 20px;
      border: 1px solid rgba(240,193,75,0.2);
    }
    .hero-subtitle::before {
      content: '';
      position: absolute;
      inset: 0;
      border-radius: 20px;
      padding: 2px;
      background: linear-gradient(135deg, var(--gold), var(--purple), var(--teal), var(--rose));
      background-size: 300% 300%;
      -webkit-mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
      -webkit-mask-composite: xor;
      mask-composite: exclude;
      animation: borderGlow 4s ease-in-out infinite;
      opacity: 0.5;
    }
    @keyframes borderGlow {
      0%, 100% { background-position: 0% 50%; opacity: 0.5; }
      50% { background-position: 100% 50%; opacity: 0.8; }
    }
    .hero-subtitle .highlight-gold {
      color: var(--gold);
      font-weight: 600;
      text-shadow: 0 0 20px rgba(240,193,75,0.5);
    }
    .hero-subtitle .highlight-purple {
      color: var(--purple);
      font-weight: 600;
      text-shadow: 0 0 20px rgba(168,85,247,0.5);
    }
    .hero-subtitle .highlight-teal {
      color: var(--teal);
      font-weight: 600;
      text-shadow: 0 0 20px rgba(20,184,166,0.5);
    }
    .hero-subtitle .highlight-rose {
      color: var(--rose);
      font-weight: 600;
      text-shadow: 0 0 20px rgba(244,63,94,0.5);
    }
    .hero-subtitle .text-glow {
      background: linear-gradient(90deg, var(--gold), var(--purple), var(--teal));
      background-size: 200% 200%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 3s ease-in-out infinite;
      font-weight: 700;
    }

    .hero-buttons {
      display: flex;
      gap: 20px;
      flex-wrap: wrap;
      animation: fadeSlideUp 1s ease 1.3s both;
    }

    .btn {
      display: inline-flex;
      align-items: center;
      gap: 12px;
      padding: 18px 36px;
      border-radius: 100px;
      font-size: 15px;
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      border: none;
      position: relative;
      overflow: hidden;
      transition: var(--transition-bounce);
      font-family: inherit;
    }

    /* Shimmer effect */
    @keyframes shimmer {
      0% { background-position: -1000px 0; }
      100% { background-position: 1000px 0; }
    }
    .btn-primary {
      background: var(--gradient-gold);
      color: #0a0a12;
      box-shadow: 0 10px 40px rgba(240, 193, 75, 0.3);
      position: relative;
      overflow: hidden;
    }
    .btn-primary::after {
      content: '';
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
      animation: shimmer 3s infinite;
    }
    .btn-primary::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(90deg, transparent, rgba(255,255,255,0.4), transparent);
      transform: translateX(-100%);
      transition: transform 0.6s ease;
    }
    .btn-primary:hover {
      transform: translateY(-5px) scale(1.02);
      box-shadow: var(--glow-gold);
    }
    .btn-primary:hover::before {
      transform: translateX(100%);
    }
    .btn-secondary {
      background: rgba(168, 85, 247, 0.15);
      color: var(--purple);
      border: 2px solid var(--purple);
    }
    .btn-secondary:hover {
      background: var(--gradient-purple);
      color: white;
      border-color: transparent;
      transform: translateY(-5px);
      box-shadow: var(--glow-purple);
    }
    .btn-teal {
      background: var(--gradient-teal);
      color: white;
      box-shadow: 0 10px 40px rgba(20, 184, 166, 0.3);
    }
    .btn-teal:hover {
      transform: translateY(-5px) scale(1.02);
      box-shadow: var(--glow-teal);
    }
    .btn-icon {
      width: 18px;
      height: 18px;
      transition: transform 0.3s ease;
    }
    .btn:hover .btn-icon {
      transform: translateX(5px);
    }

    .hero-stats {
      display: flex;
      gap: 50px;
      margin-top: 60px;
      animation: fadeSlideUp 1s ease 1.5s both;
    }
    .stat {
      position: relative;
    }
    .stat::after {
      content: '';
      position: absolute;
      right: -25px;
      top: 50%;
      transform: translateY(-50%);
      width: 2px;
      height: 40px;
      background: linear-gradient(180deg, transparent, var(--purple), transparent);
    }
    .stat:last-child::after { display: none; }
    .stat-number {
      font-family: 'Cormorant Garamond', serif;
      font-size: 52px;
      font-weight: 700;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 4s ease-in-out infinite;
      line-height: 1;
    }
    .stat-label {
      font-size: 12px;
      color: var(--text-desc);
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-top: 5px;
    }

    /* Hero Image */
    .hero-image {
      position: relative;
      animation: fadeSlideUp 1s ease 0.8s both;
    }
    .hero-image-wrapper {
      position: relative;
      width: 100%;
      max-width: 480px;
      margin: 0 auto;
    }
    .hero-image-frame {
      position: relative;
      border-radius: 30px;
      overflow: hidden;
      border: 4px solid transparent;
      background: linear-gradient(var(--bg-dark), var(--bg-dark)) padding-box,
                  var(--gradient-rainbow) border-box;
      box-shadow: 0 30px 60px rgba(0,0,0,0.5), var(--glow-purple);
      animation: borderPulse 4s ease-in-out infinite;
    }
    @keyframes borderPulse {
      0%, 100% { filter: brightness(1); }
      50% { filter: brightness(1.2); }
    }
    .hero-image-frame img {
      width: 100%;
      height: auto;
      display: block;
      object-fit: cover;
      aspect-ratio: 4/5;
    }
    .hero-image-info {
      position: absolute;
      bottom: 0;
      left: 0;
      right: 0;
      background: linear-gradient(transparent, rgba(10, 10, 18, 0.95));
      padding: 40px 25px 25px;
    }
    .hero-image-info h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 28px;
      font-weight: 700;
      background: var(--gradient-gold);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      margin-bottom: 5px;
    }
    .hero-image-info p {
      font-size: 14px;
      color: var(--teal);
      font-weight: 500;
    }

    /* ===== CREDENTIALS SHOWCASE ===== */
    .credentials-section {
      padding: 60px 40px;
      position: relative;
      overflow: hidden;
      background: linear-gradient(180deg, rgba(168,85,247,0.05), transparent, rgba(20,184,166,0.05));
    }
    .credentials-container {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;
    }
    .credential-card {
      background: linear-gradient(145deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 35px;
      text-align: center;
      position: relative;
      overflow: hidden;
      transition: var(--transition-bounce);
    }
    .credential-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      animation: rainbowShift 5s ease-in-out infinite;
      transform: scaleX(0);
      transition: transform 0.4s ease;
      transform-origin: left;
    }
    .credential-card:hover::before {
      transform: scaleX(1);
    }
    .credential-card:hover {
      transform: translateY(-10px) scale(1.02);
      border-color: var(--purple);
    }
    
    /* Different animations for each card */
    .credential-card:nth-child(1) {
      animation: floatUpDown 4s ease-in-out infinite;
    }
    .credential-card:nth-child(2) {
      animation: floatLeftRight 5s ease-in-out infinite;
    }
    .credential-card:nth-child(3) {
      animation: floatRotate 6s ease-in-out infinite;
    }
    
    @keyframes floatUpDown {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-15px); }
    }
    @keyframes floatLeftRight {
      0%, 100% { transform: translateX(0); }
      50% { transform: translateX(10px); }
    }
    @keyframes floatRotate {
      0%, 100% { transform: rotate(0deg) translateY(0); }
      25% { transform: rotate(1deg) translateY(-8px); }
      75% { transform: rotate(-1deg) translateY(-5px); }
    }
    
    .credential-card:nth-child(1):hover { 
      animation: none;
      box-shadow: var(--glow-gold);
    }
    .credential-card:nth-child(2):hover { 
      animation: none;
      box-shadow: var(--glow-purple);
    }
    .credential-card:nth-child(3):hover { 
      animation: none;
      box-shadow: var(--glow-teal);
    }
    
    .credential-icon {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 20px;
      font-size: 36px;
      position: relative;
    }
    .credential-card:nth-child(1) .credential-icon {
      background: var(--gradient-gold);
      box-shadow: var(--glow-gold);
      animation: iconPulse 2s ease-in-out infinite;
    }
    .credential-card:nth-child(2) .credential-icon {
      background: var(--gradient-purple);
      box-shadow: var(--glow-purple);
      animation: iconSpin 8s linear infinite;
    }
    .credential-card:nth-child(3) .credential-icon {
      background: var(--gradient-teal);
      box-shadow: var(--glow-teal);
      animation: iconBounce 2s ease-in-out infinite;
    }
    
    @keyframes iconPulse {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.1); }
    }
    @keyframes iconSpin {
      0% { transform: rotate(0deg); }
      100% { transform: rotate(360deg); }
    }
    @keyframes iconBounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-10px); }
    }
    
    .credential-card h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 24px;
      font-weight: 700;
      margin-bottom: 10px;
      transition: var(--transition);
    }
    .credential-card:nth-child(1) h3 { color: var(--gold); }
    .credential-card:nth-child(2) h3 { color: var(--purple); }
    .credential-card:nth-child(3) h3 { color: var(--teal); }
    
    .credential-card p {
      font-size: 14px;
      color: var(--text-desc);
      line-height: 1.7;
    }
    .credential-card:hover h3 {
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 3s ease-in-out infinite;
    }

    /* ===== MARQUEE ===== */
    .marquee-section {
      padding: 40px 0;
      border-top: 1px solid var(--border);
      border-bottom: 1px solid var(--border);
      overflow: hidden;
      background: linear-gradient(90deg, rgba(240,193,75,0.03), rgba(168,85,247,0.03), rgba(20,184,166,0.03));
    }
    .marquee {
      display: flex;
      animation: marquee 30s linear infinite;
    }
    .marquee-item {
      display: flex;
      align-items: center;
      gap: 15px;
      padding: 0 50px;
      white-space: nowrap;
    }
    .marquee-item .icon {
      font-size: 28px;
    }
    .marquee-item .text {
      font-family: 'Cormorant Garamond', serif;
      font-size: 22px;
      font-weight: 600;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 5s ease-in-out infinite;
    }
    @keyframes marquee {
      0% { transform: translateX(0); }
      100% { transform: translateX(-50%); }
    }

    /* ===== SECTIONS ===== */
    section {
      padding: 120px 40px;
      position: relative;
    }
    .container {
      max-width: 1200px;
      margin: 0 auto;
    }
    .section-header {
      text-align: center;
      margin-bottom: 80px;
    }
    .section-tag {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      background: linear-gradient(135deg, rgba(168,85,247,0.15), rgba(20,184,166,0.15));
      border: 1px solid var(--border-purple);
      padding: 10px 24px;
      border-radius: 100px;
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 3px;
      margin-bottom: 20px;
    }
    .section-tag span {
      background: linear-gradient(90deg, var(--purple), var(--teal));
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
    }
    .section-title {
      font-family: 'Cormorant Garamond', serif;
      font-size: clamp(36px, 5vw, 56px);
      font-weight: 700;
      letter-spacing: -1px;
      margin-bottom: 20px;
      color: var(--primary);
      animation: titleGlow 3s ease-in-out infinite;
    }
    @keyframes titleGlow {
      0%, 100% { text-shadow: 0 0 20px rgba(240, 193, 75, 0.3); }
      50% { text-shadow: 0 0 30px rgba(168, 85, 247, 0.5), 0 0 40px rgba(240, 193, 75, 0.3); }
    }
    .section-title .colored {
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 5s ease-in-out infinite;
    }
    .section-subtitle {
      font-size: 17px;
      color: var(--text-desc);
      max-width: 600px;
      margin: 0 auto;
      line-height: 1.8;
    }

    /* ===== ADMIN SECTION ===== */
    #admin {
      background: linear-gradient(180deg, rgba(240,193,75,0.03), transparent);
      padding-top: 80px;
    }
    .admin-container {
      max-width: 1000px;
      margin: 0 auto;
    }
    .admin-login-card {
      max-width: 500px;
      margin: 0 auto;
      background: linear-gradient(145deg, rgba(255,255,255,0.05), transparent);
      border: 2px solid var(--border);
      border-radius: 30px;
      padding: 50px;
      text-align: center;
    }
    .admin-login-card .lock-icon {
      width: 100px;
      height: 100px;
      border-radius: 50%;
      background: var(--gradient-purple);
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 30px;
      box-shadow: var(--glow-purple);
    }
    .admin-login-card .lock-icon svg {
      width: 50px;
      height: 50px;
      color: white;
    }
    .admin-login-card h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 32px;
      font-weight: 700;
      margin-bottom: 10px;
    }
    .admin-login-card > p {
      color: var(--text-desc);
      margin-bottom: 30px;
    }

    .admin-panel {
      display: none;
    }
    .admin-panel.active {
      display: block;
      animation: fadeSlideUp 0.6s ease;
    }
    .admin-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 40px;
      padding-bottom: 20px;
      border-bottom: 1px solid var(--border);
    }
    .admin-header h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 32px;
      font-weight: 700;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 4s ease-in-out infinite;
    }
    .admin-tabs {
      display: flex;
      gap: 10px;
      margin-bottom: 30px;
    }
    .admin-tab {
      padding: 12px 30px;
      border-radius: 100px;
      background: rgba(255,255,255,0.05);
      border: 1px solid var(--border);
      color: var(--secondary);
      font-weight: 600;
      cursor: pointer;
      transition: var(--transition);
    }
    .admin-tab:hover, .admin-tab.active {
      background: var(--gradient-purple);
      color: white;
      border-color: transparent;
    }
    .admin-content {
      display: none;
    }
    .admin-content.active {
      display: block;
    }

    /* Cases Management */
    .case-form-card {
      background: linear-gradient(145deg, rgba(255,255,255,0.04), transparent);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 40px;
      margin-bottom: 40px;
    }
    .case-form-card h4 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 24px;
      font-weight: 700;
      margin-bottom: 25px;
      color: var(--gold);
    }

    .cases-list {
      display: grid;
      gap: 20px;
    }
    .case-item {
      background: linear-gradient(145deg, rgba(255,255,255,0.03), transparent);
      border: 1px solid var(--border);
      border-radius: 16px;
      padding: 25px;
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 20px;
      align-items: center;
      transition: var(--transition);
    }
    .case-item:hover {
      border-color: var(--purple);
      background: rgba(168, 85, 247, 0.05);
    }
    .case-info h5 {
      font-size: 18px;
      font-weight: 700;
      margin-bottom: 5px;
      color: var(--gold);
    }
    .case-info p {
      font-size: 14px;
      color: var(--text-desc);
      margin-bottom: 3px;
    }
    .case-meta {
      display: flex;
      gap: 15px;
      margin-top: 10px;
    }
    .case-tag {
      padding: 5px 15px;
      border-radius: 100px;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
    }
    .case-tag.pending {
      background: linear-gradient(135deg, rgba(240,193,75,0.2), rgba(249,115,22,0.2));
      color: var(--gold);
      border: 1px solid rgba(240,193,75,0.3);
    }
    .case-tag.active {
      background: linear-gradient(135deg, rgba(16,185,129,0.2), rgba(20,184,166,0.2));
      color: var(--emerald);
      border: 1px solid rgba(16,185,129,0.3);
    }
    .case-tag.closed {
      background: rgba(156,163,175,0.2);
      color: var(--secondary);
      border: 1px solid rgba(156,163,175,0.3);
    }
    .case-actions {
      display: flex;
      gap: 10px;
    }
    .case-btn {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      border: none;
      cursor: pointer;
      transition: var(--transition);
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .case-btn.edit {
      background: var(--gradient-teal);
    }
    .case-btn.delete {
      background: var(--gradient-rose);
    }
    .case-btn:hover {
      transform: scale(1.1);
    }
    .case-btn svg {
      width: 18px;
      height: 18px;
      color: white;
    }

    .empty-state {
      text-align: center;
      padding: 60px;
      color: var(--secondary);
    }
    .empty-state .icon {
      font-size: 60px;
      margin-bottom: 20px;
      opacity: 0.5;
    }

    /* ===== SERVICES ===== */
    .services-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;
    }
    .service-card {
      background: linear-gradient(145deg, rgba(255,255,255,0.04), rgba(255,255,255,0.01));
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 40px;
      position: relative;
      overflow: hidden;
      cursor: pointer;
      transition: var(--transition-bounce);
    }
    .service-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      animation: rainbowShift 5s ease-in-out infinite;
      transform: scaleX(0);
      transition: transform 0.4s ease;
    }
    .service-card:hover::before { transform: scaleX(1); }

    /* Pulsing glow effect for service cards */
    @keyframes pulseGlow {
      0%, 100% { box-shadow: 0 20px 50px rgba(168, 85, 247, 0.2); }
      50% { box-shadow: 0 20px 60px rgba(168, 85, 247, 0.4), 0 0 30px rgba(240, 193, 75, 0.2); }
    }
    .service-card:hover {
      transform: translateY(-10px);
      border-color: var(--purple);
      animation: pulseGlow 2s ease-in-out infinite;
    }
    .service-number {
      position: absolute;
      top: 20px;
      right: 25px;
      font-family: 'Cormorant Garamond', serif;
      font-size: 60px;
      font-weight: 700;
      background: linear-gradient(180deg, rgba(168,85,247,0.2), transparent);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      line-height: 1;
    }
    .service-icon {
      width: 70px;
      height: 70px;
      border-radius: 20px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 25px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.3);
      transition: var(--transition-bounce);
    }
    .service-card:nth-child(1) .service-icon { background: var(--gradient-gold); }
    .service-card:nth-child(2) .service-icon { background: var(--gradient-purple); }
    .service-card:nth-child(3) .service-icon { background: var(--gradient-teal); }
    .service-card:nth-child(4) .service-icon { background: var(--gradient-blue); }
    .service-card:nth-child(5) .service-icon { background: var(--gradient-rose); }
    .service-card:nth-child(6) .service-icon { background: linear-gradient(135deg, var(--orange), var(--gold)); }
    .service-card:hover .service-icon {
      transform: scale(1.1) rotate(-5deg);
    }
    .service-icon svg {
      width: 32px;
      height: 32px;
      color: #0a0a12;
    }
    .service-card h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 24px;
      font-weight: 700;
      margin-bottom: 12px;
      color: var(--primary);
      transition: var(--transition);
    }
    .service-card:hover h3 { color: var(--gold); }
    .service-card p {
      font-size: 14px;
      color: var(--text-desc);
      line-height: 1.8;
    }

    /* ===== TEAM ===== */
    #team {
      background: linear-gradient(180deg, rgba(168,85,247,0.03), transparent, rgba(20,184,166,0.03));
    }
    .team-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 30px;
    }
    .team-card {
      background: linear-gradient(145deg, rgba(255,255,255,0.04), transparent);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 30px;
      text-align: center;
      transition: var(--transition-bounce);
      position: relative;
      overflow: hidden;
    }
    .team-card::before {
      content: '';
      position: absolute;
      inset: 0;
      background: var(--gradient-rainbow);
      opacity: 0;
      transition: opacity 0.4s ease;
    }
    .team-card:hover::before { opacity: 0.05; }
    .team-card:hover {
      transform: translateY(-10px);
      border-color: var(--teal);
      box-shadow: 0 20px 50px rgba(20, 184, 166, 0.2);
    }
    .team-img-wrapper {
      width: 140px;
      height: 140px;
      margin: 0 auto 20px;
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      border: 3px solid transparent;
      background: linear-gradient(var(--bg-dark), var(--bg-dark)) padding-box,
                  var(--gradient-rainbow) border-box;
    }
    .team-img {
      width: 100%;
      height: 100%;
      object-fit: cover;
    }
    .team-badge {
      position: absolute;
      bottom: -5px;
      right: -5px;
      width: 36px;
      height: 36px;
      border-radius: 10px;
      background: var(--gradient-teal);
      display: flex;
      align-items: center;
      justify-content: center;
      border: 3px solid var(--bg-dark);
      box-shadow: 0 5px 15px rgba(20, 184, 166, 0.4);
      animation: badgeBounce 2s ease-in-out infinite;
    }
    @keyframes badgeBounce {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-5px); }
    }
    .team-badge svg {
      width: 16px;
      height: 16px;
      color: white;
    }
    .team-card h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 22px;
      font-weight: 700;
      margin-bottom: 8px;
      transition: var(--transition);
    }
    .team-card:hover h3 {
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 3s ease-in-out infinite;
    }
    .team-card .role {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 2px;
      margin-bottom: 12px;
      color: var(--teal);
    }
    .team-card p {
      font-size: 14px;
      color: var(--text-desc);
      line-height: 1.7;
    }

    /* ===== APPOINTMENT ===== */
    .appointment-wrapper {
      display: grid;
      grid-template-columns: 1fr 1.2fr;
      gap: 60px;
      align-items: start;
    }
    .appointment-info h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 42px;
      font-weight: 700;
      letter-spacing: -1px;
      margin-bottom: 20px;
      line-height: 1.1;
    }
    .appointment-info h3 .colored {
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 4s ease-in-out infinite;
    }
    .appointment-info > p {
      font-size: 16px;
      color: var(--text-desc);
      margin-bottom: 40px;
      line-height: 1.8;
    }
    .info-item {
      display: flex;
      gap: 20px;
      padding: 24px;
      background: rgba(255,255,255,0.02);
      border: 1px solid var(--border);
      border-radius: 16px;
      margin-bottom: 16px;
      transition: var(--transition);
    }
    .info-item:hover {
      transform: translateX(10px);
      border-color: var(--purple);
      background: rgba(168, 85, 247, 0.05);
    }
    .info-icon {
      width: 54px;
      height: 54px;
      border-radius: 14px;
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }
    .info-item:nth-child(1) .info-icon { background: var(--gradient-gold); }
    .info-item:nth-child(2) .info-icon { background: var(--gradient-purple); }
    .info-item:nth-child(3) .info-icon { background: var(--gradient-teal); }
    .info-icon svg {
      width: 26px;
      height: 26px;
      color: #0a0a12;
    }
    .info-item h4 {
      font-size: 16px;
      font-weight: 700;
      margin-bottom: 4px;
    }
    .info-item p {
      font-size: 14px;
      color: var(--text-desc);
    }

    .form-card {
      background: linear-gradient(145deg, rgba(255,255,255,0.04), transparent);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 45px;
      position: relative;
      overflow: hidden;
    }
    .form-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 4px;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      animation: rainbowShift 5s ease-in-out infinite;
    }
    .form-card h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 28px;
      font-weight: 700;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 4s ease-in-out infinite;
      margin-bottom: 8px;
    }
    .form-card > p {
      font-size: 14px;
      color: var(--text-desc);
      margin-bottom: 30px;
    }
    .form-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 20px;
    }
    .form-group {
      position: relative;
    }
    .form-group.full { grid-column: 1 / -1; }
    .form-group label {
      display: block;
      font-size: 13px;
      font-weight: 600;
      margin-bottom: 8px;
      color: var(--primary);
    }
    .form-group input,
    .form-group textarea,
    .form-group select {
      width: 100%;
      padding: 16px 20px;
      border-radius: 12px;
      border: 2px solid var(--border);
      background: rgba(0,0,0,0.3);
      color: var(--primary);
      font-family: inherit;
      font-size: 15px;
      transition: var(--transition);
    }
    .form-group input:focus,
    .form-group textarea:focus,
    .form-group select:focus {
      outline: none;
      border-color: var(--purple);
      box-shadow: 0 0 20px rgba(168, 85, 247, 0.2);
    }
    .form-group input::placeholder,
    .form-group textarea::placeholder { color: var(--secondary); }
    .form-group textarea {
      min-height: 120px;
      resize: vertical;
    }
    .form-disclaimer {
      font-size: 12px;
      color: var(--text-desc);
      margin: 24px 0;
      padding: 16px;
      background: linear-gradient(135deg, rgba(240,193,75,0.08), rgba(168,85,247,0.08));
      border-radius: 12px;
      border-left: 4px solid var(--purple);
    }
    .form-submit { width: 100%; }
    .form-status {
      margin-top: 20px;
      padding: 16px;
      border-radius: 12px;
      font-size: 14px;
      display: none;
    }
    .form-status.success {
      display: block;
      background: linear-gradient(135deg, rgba(16,185,129,0.15), rgba(20,184,166,0.15));
      border: 1px solid rgba(16,185,129,0.3);
      color: var(--emerald);
    }
    .form-status.error {
      display: block;
      background: rgba(239,68,68,0.1);
      border: 1px solid rgba(239,68,68,0.3);
      color: var(--rose);
    }
    .form-status.loading {
      display: block;
      background: linear-gradient(135deg, rgba(240,193,75,0.15), rgba(168,85,247,0.15));
      border: 1px solid var(--border);
      color: var(--gold);
    }

    /* ===== CONTACT ===== */
    .contact-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 30px;
      margin-bottom: 60px;
    }
    .contact-card {
      background: linear-gradient(145deg, rgba(255,255,255,0.04), transparent);
      border: 1px solid var(--border);
      border-radius: 24px;
      padding: 40px;
      text-align: center;
      transition: var(--transition-bounce);
    }
    .contact-card:hover {
      transform: translateY(-10px);
      border-color: var(--teal);
      box-shadow: var(--glow-teal);
    }
    .contact-icon {
      width: 80px;
      height: 80px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 0 auto 20px;
      transition: var(--transition-bounce);
    }
    .contact-card:nth-child(1) .contact-icon { background: var(--gradient-purple); box-shadow: var(--glow-purple); }
    .contact-card:nth-child(2) .contact-icon { background: var(--gradient-teal); box-shadow: var(--glow-teal); }
    .contact-card:nth-child(3) .contact-icon { background: var(--gradient-gold); box-shadow: var(--glow-gold); }
    .contact-card:hover .contact-icon {
      transform: scale(1.1) rotate(-10deg);
    }
    .contact-icon svg {
      width: 34px;
      height: 34px;
      color: #0a0a12;
    }
    .contact-card h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 22px;
      font-weight: 700;
      margin-bottom: 10px;
    }
    .contact-card p {
      font-size: 14px;
      color: var(--text-desc);
      line-height: 1.7;
    }

    /* ===== FOOTER ===== */
    footer {
      background: linear-gradient(180deg, transparent, rgba(0,0,0,0.5));
      border-top: 1px solid var(--border);
      padding: 80px 40px 30px;
      position: relative;
    }
    footer::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      animation: rainbowShift 5s ease-in-out infinite;
    }
    .footer-grid {
      max-width: 1200px;
      margin: 0 auto;
      display: grid;
      grid-template-columns: 2fr 1fr 1fr 1fr;
      gap: 60px;
      margin-bottom: 60px;
    }
    .footer-brand h3 {
      font-family: 'Cormorant Garamond', serif;
      font-size: 28px;
      font-weight: 700;
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 4s ease-in-out infinite;
      margin-bottom: 16px;
    }
    .footer-brand p {
      font-size: 14px;
      color: var(--text-desc);
      line-height: 1.8;
      margin-bottom: 24px;
    }
    .footer-social {
      display: flex;
      gap: 12px;
    }
    .footer-social a {
      width: 48px;
      height: 48px;
      border-radius: 14px;
      background: rgba(255,255,255,0.05);
      border: 1px solid var(--border);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition);
    }
    .footer-social a:hover {
      background: var(--gradient-purple);
      border-color: transparent;
      transform: translateY(-5px);
      box-shadow: var(--glow-purple);
    }
    .footer-social a svg {
      width: 20px;
      height: 20px;
      color: var(--secondary);
      transition: var(--transition);
    }
    .footer-social a:hover svg { color: white; }
    .footer-col h4 {
      font-size: 13px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 2px;
      color: var(--teal);
      margin-bottom: 24px;
    }
    .footer-col ul { list-style: none; }
    .footer-col li { margin-bottom: 14px; }
    .footer-col a {
      font-size: 14px;
      color: var(--text-desc);
      text-decoration: none;
      transition: var(--transition);
    }
    .footer-col a:hover {
      color: var(--gold);
      padding-left: 10px;
    }
    .footer-bottom {
      max-width: 1200px;
      margin: 0 auto;
      border-top: 1px solid var(--border);
      padding-top: 30px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 15px;
    }
    .footer-bottom p {
      font-size: 13px;
      color: var(--secondary);
    }
    .footer-bottom span {
      background: var(--gradient-rainbow);
      background-size: 300% 300%;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      background-clip: text;
      animation: rainbowShift 4s ease-in-out infinite;
      font-weight: 600;
    }

    /* ===== SCROLL REVEAL ===== */
    .reveal {
      opacity: 0;
      transform: translateY(50px);
      transition: all 0.8s var(--transition-elastic);
    }
    .reveal.active {
      opacity: 1;
      transform: translateY(0);
    }
    .stagger > * {
      opacity: 0;
      transform: translateY(30px);
      transition: all 0.6s var(--transition-elastic);
    }
    .stagger.active > *:nth-child(1) { transition-delay: 0.1s; opacity: 1; transform: translateY(0); }
    .stagger.active > *:nth-child(2) { transition-delay: 0.2s; opacity: 1; transform: translateY(0); }
    .stagger.active > *:nth-child(3) { transition-delay: 0.3s; opacity: 1; transform: translateY(0); }
    .stagger.active > *:nth-child(4) { transition-delay: 0.4s; opacity: 1; transform: translateY(0); }
    .stagger.active > *:nth-child(5) { transition-delay: 0.5s; opacity: 1; transform: translateY(0); }
    .stagger.active > *:nth-child(6) { transition-delay: 0.6s; opacity: 1; transform: translateY(0); }

    /* ===== RESPONSIVE ===== */
    @media (max-width: 1024px) {
      .hero-container { grid-template-columns: 1fr; text-align: center; }
      .hero-image { order: -1; }
      .hero-image-wrapper { max-width: 380px; }
      .hero-subtitle { margin: 0 auto 40px; }
      .hero-stats { justify-content: center; }
      .services-grid { grid-template-columns: repeat(2, 1fr); }
      .appointment-wrapper { grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: 1fr 1fr; }
      .credentials-container { grid-template-columns: 1fr; }
    }
    @media (max-width: 768px) {
      .nav-wrapper { padding: 15px 20px; }
      .nav-links { display: none; }
      .menu-btn { display: flex; align-items: center; justify-content: center; }
      .hero { padding: 120px 20px 80px; }
      .hero-stats { flex-direction: column; gap: 30px; }
      .hero-stats .stat::after { display: none; }
      section { padding: 80px 20px; }
      .services-grid, .contact-grid { grid-template-columns: 1fr; }
      .form-grid { grid-template-columns: 1fr; }
      .footer-grid { grid-template-columns: 1fr; gap: 40px; }
      .footer-bottom { flex-direction: column; text-align: center; }
      .disclaimer-modal { padding: 30px 25px; }
      .disclaimer-buttons { flex-direction: column; }
      .admin-header { flex-direction: column; gap: 15px; text-align: center; }
      .admin-tabs { flex-wrap: wrap; justify-content: center; }
      .credentials-section { padding: 40px 20px; }
    }
    @media (max-width: 480px) {
      .hero-title { font-size: 36px; }
      .section-title { font-size: 28px; }
      .btn { width: 100%; justify-content: center; }
      .hero-buttons { flex-direction: column; }
      .hero-subtitle { padding: 20px; font-size: 16px; }
    }
  </style>
</head>
<body>
  <!-- Preloader -->
  <div class="preloader" id="preloader">
    <div class="preloader-icon">
      <div class="preloader-ring"></div>
    </div>
    <div class="preloader-logo">Surse Law Firm</div>
    <div class="preloader-tagline">Justice • Integrity • Excellence</div>
    <div class="preloader-bar"></div>
  </div>

  <!-- Background Effects -->
  <div class="bg-effects">
    <div class="gradient-orbs">
      <div class="orb orb-gold"></div>
      <div class="orb orb-purple"></div>
      <div class="orb orb-teal"></div>
      <div class="orb orb-rose"></div>
    </div>
    <div class="grid-pattern"></div>
    <div class="floating-icons">
      <div class="float-icon">⚖️</div>
      <div class="float-icon">📜</div>
      <div class="float-icon">🏛️</div>
      <div class="float-icon">📋</div>
      <div class="float-icon">⚖️</div>
    </div>
  </div>

  <!-- Disclaimer Popup -->
  <div class="disclaimer-overlay" id="disclaimerOverlay">
    <div class="disclaimer-modal">
      <div class="disclaimer-header">
        <div class="disclaimer-icon">⚖️</div>
        <h2>Legal Disclaimer</h2>
        <p>As per Bar Council of India Rules</p>
      </div>

      <div class="disclaimer-content">
        <h3>⚖️ Important Notice</h3>
        <p><strong>This website is for informational purposes only</strong> and does not constitute legal advice or create an advocate-client relationship.</p>
        <p>As per the rules laid down by the <strong>Bar Council of India</strong>, we are not permitted to solicit work and advertise.</p>
        
        <ul class="disclaimer-list">
          <li>Viewing this website does not create an advocate-client relationship</li>
          <li>Information provided is not to be construed as legal advice</li>
          <li>We comply with the Advocates Act, 1961 and Bar Council of India Rules</li>
          <li>Your personal data is protected under the Digital Personal Data Protection Act, 2023</li>
          <li>Past results do not guarantee similar outcomes in future matters</li>
        </ul>
        
        <p>The user wishes to gain more information about the firm for their own information and use. The information about the firm is provided to the user only on their specific request.</p>
      </div>

      <div class="disclaimer-checkbox" onclick="document.getElementById('agreeCheck').click()">
        <input type="checkbox" id="agreeCheck" onchange="toggleAgreeButton()">
        <label for="agreeCheck">I have read and understood the above disclaimer. I agree to proceed at my own risk and confirm that I am seeking information about the firm on my own accord.</label>
      </div>

      <div class="disclaimer-buttons">
        <button class="btn-exit" onclick="window.location.href='https://www.google.com'">Exit Website</button>
        <button class="btn-agree" id="agreeBtn" disabled onclick="acceptDisclaimer()">
          I Agree & Enter
          <svg style="width:18px;height:18px;margin-left:8px" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
        </button>
      </div>
    </div>
  </div>

  <!-- Navigation -->
  <div class="nav-wrapper" id="navbar">
    <div class="nav-container">
      <a href="#home" class="logo">
        <div class="logo-icon">S</div>
        <span class="logo-text">Surse Law Firm</span>
      </a>
      <ul class="nav-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#admin">Admin</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#team">Team</a></li>
        <li><a href="#appointment">Appointment</a></li>
        <li><a href="#contact">Contact</a></li>
        <li><a href="#appointment" class="nav-cta">Book Consultation</a></li>
      </ul>
      <button class="menu-btn" id="menuBtn">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </div>

  <!-- Mobile Navigation -->
  <div class="mobile-nav" id="mobileNav">
    <a href="#home">Home</a>
    <a href="#admin">Admin</a>
    <a href="#services">Services</a>
    <a href="#team">Team</a>
    <a href="#appointment">Appointment</a>
    <a href="#contact">Contact</a>
  </div>

  <!-- Hero Section -->
  <section class="hero" id="home">
    <div class="hero-container">
      <div class="hero-content">
        <div class="hero-badge">
          <span class="pulse-dot"></span>
          <span>Established Legal Practice • Est. 2009</span>
        </div>

        <h1 class="hero-title">
          <span class="line"><span>Trusted Legal</span></span>
          <span class="line"><span class="gradient-text">Excellence</span></span>
          <span class="line"><span>Since 15+ Years</span></span>
        </h1>
        
        <p class="hero-subtitle">
          <span class="highlight-gold">Surse Law Firm</span> delivers distinguished legal counsel across <span class="highlight-purple">Corporate</span>, <span class="highlight-teal">Family</span>, <span class="highlight-rose">Property</span>, and <span class="highlight-gold">Litigation</span> matters. We are committed to upholding <span class="text-glow">justice with integrity</span>, professionalism, and unwavering dedication to our clients' interests under Indian law.
        </p>
        
        <div class="hero-buttons">
          <a href="#appointment" class="btn btn-primary">
            <span>Schedule Consultation</span>
            <svg class="btn-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </a>
          <a href="#services" class="btn btn-secondary">
            <span>View Practice Areas</span>
          </a>
        </div>
        
        <div class="hero-stats">
          <div class="stat">
            <div class="stat-number">15+</div>
            <div class="stat-label">Years Experience</div>
          </div>
          <div class="stat">
            <div class="stat-number">500+</div>
            <div class="stat-label">Cases Handled</div>
          </div>
          <div class="stat">
            <div class="stat-number">6</div>
            <div class="stat-label">Practice Areas</div>
          </div>
        </div>
      </div>

      <div class="hero-image">
        <div class="hero-image-wrapper">
          <div class="hero-image-frame">
            <img src="https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=600&h=750&fit=crop" alt="Lead Advocate - Surse Law Firm">
            <div class="hero-image-info">
              <h3>Adv. Sunil Surse</h3>
              <p>Lead Advocate & Founder</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Credentials Showcase Section -->
  <div class="credentials-section">
    <div class="credentials-container">
      <div class="credential-card">
        <div class="credential-icon">⚖️</div>
        <h3>Bar Council Enrolled</h3>
        <p>Registered Advocate with the Bar Council of India, practicing law with full compliance to ethical standards and regulations.</p>
      </div>
      <div class="credential-card">
        <div class="credential-icon">🏛️</div>
        <h3>High Court Practice</h3>
        <p>Extensive practice across all District Courts and appearances in the High Court for complex litigation matters.</p>
      </div>
      <div class="credential-card">
        <div class="credential-icon">📜</div>
        <h3>Documentation Expert</h3>
        <p>Specialized in legal drafting, contract preparation, agreements, and comprehensive documentation services.</p>
      </div>
    </div>
  </div>

  <!-- Admin Section (Moved to Top) -->
  <section id="admin">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag"><span>🔐 Secure Access</span></span>
        <h2 class="section-title">Admin <span class="colored">Panel</span></h2>
        <p class="section-subtitle">Secure case management system for authorized personnel only.</p>
      </div>

      <div class="admin-container">
        <!-- Login Card -->
        <div class="admin-login-card reveal" id="adminLoginCard">
          <div class="lock-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
          </div>
          <h3>Admin Login</h3>
          <p>Enter your credentials to access case management</p>
          
          <form id="adminLoginForm" style="margin-top: 30px;">
            <div class="form-group">
              <label for="adminUser">Username</label>
              <input type="text" id="adminUser" placeholder="Enter username" required>
            </div>
            <div class="form-group" style="margin-top: 15px;">
              <label for="adminPass">Password</label>
              <input type="password" id="adminPass" placeholder="Enter password" required>
            </div>
            <button type="submit" class="btn btn-primary" style="width: 100%; margin-top: 25px;">
              <span>Login to Panel</span>
              <svg class="btn-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"/></svg>
            </button>
          </form>
          <p id="adminLoginStatus" class="form-status"></p>
        </div>

        <!-- Admin Panel -->
        <div class="admin-panel" id="adminPanel">
          <div class="admin-header">
            <h3>⚖️ Case Management System</h3>
            <button class="btn btn-secondary" onclick="adminLogout()">
              <svg style="width:18px;height:18px" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1"/></svg>
              <span>Logout</span>
            </button>
          </div>

          <div class="admin-tabs">
            <button class="admin-tab active" onclick="switchTab('cases')">📁 All Cases</button>
            <button class="admin-tab" onclick="switchTab('add')">➕ Add New Case</button>
            <button class="admin-tab" onclick="switchTab('appointments')">📅 Appointments</button>
          </div>

          <!-- Add Case Form -->
          <div class="admin-content" id="tab-add">
            <div class="case-form-card">
              <h4>➕ Add New Case</h4>
              <form id="addCaseForm">
                <div class="form-grid">
                  <div class="form-group">
                    <label for="caseNo">Case Number *</label>
                    <input type="text" id="caseNo" required placeholder="e.g., CASE/2024/001">
                  </div>
                  <div class="form-group">
                    <label for="caseClient">Client Name *</label>
                    <input type="text" id="caseClient" required placeholder="Client full name">
                  </div>
                  <div class="form-group">
                    <label for="caseType">Case Type *</label>
                    <select id="caseType" required>
                      <option value="">Select type...</option>
                      <option>Corporate</option>
                      <option>Family</option>
                      <option>Property</option>
                      <option>Civil</option>
                      <option>Criminal</option>
                      <option>Other</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="caseStatusSelect">Status *</label>
                    <select id="caseStatusSelect" required>
                      <option value="pending">Pending</option>
                      <option value="active">Active</option>
                      <option value="closed">Closed</option>
                    </select>
                  </div>
                  <div class="form-group">
                    <label for="caseCourt">Court Name</label>
                    <input type="text" id="caseCourt" placeholder="e.g., District Court, Aurangabad">
                  </div>
                  <div class="form-group">
                    <label for="caseDate">Filing Date</label>
                    <input type="date" id="caseDate">
                  </div>
                  <div class="form-group full">
                    <label for="caseDetails">Case Details</label>
                    <textarea id="caseDetails" rows="4" placeholder="Enter detailed case information..."></textarea>
                  </div>
                </div>
                <button type="submit" class="btn btn-teal" style="margin-top: 25px;">
                  <span>Save Case</span>
                  <svg class="btn-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                </button>
                <p id="caseFormStatus" class="form-status"></p>
              </form>
            </div>
          </div>

          <!-- Cases List -->
          <div class="admin-content active" id="tab-cases">
            <div class="cases-list" id="casesList">
              <!-- Cases will be loaded here -->
            </div>
          </div>

          <!-- Appointments List -->
          <div class="admin-content" id="tab-appointments">
            <div class="cases-list" id="appointmentsList">
              <!-- Appointments will be loaded here -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Marquee -->
  <div class="marquee-section">
    <div class="marquee">
      <div class="marquee-item"><span class="icon">⚖️</span><span class="text">Corporate Law</span></div>
      <div class="marquee-item"><span class="icon">👨‍👩‍👧‍👦</span><span class="text">Family Law</span></div>
      <div class="marquee-item"><span class="icon">🏠</span><span class="text">Property Law</span></div>
      <div class="marquee-item"><span class="icon">🔒</span><span class="text">Criminal Defense</span></div>
      <div class="marquee-item"><span class="icon">📜</span><span class="text">Civil Litigation</span></div>
      <div class="marquee-item"><span class="icon">📝</span><span class="text">Legal Documentation</span></div>
      <div class="marquee-item"><span class="icon">⚖️</span><span class="text">Corporate Law</span></div>
      <div class="marquee-item"><span class="icon">👨‍👩‍👧‍👦</span><span class="text">Family Law</span></div>
      <div class="marquee-item"><span class="icon">🏠</span><span class="text">Property Law</span></div>
      <div class="marquee-item"><span class="icon">🔒</span><span class="text">Criminal Defense</span></div>
      <div class="marquee-item"><span class="icon">📜</span><span class="text">Civil Litigation</span></div>
      <div class="marquee-item"><span class="icon">📝</span><span class="text">Legal Documentation</span></div>
    </div>
  </div>

  <!-- Services -->
  <section id="services">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag"><span>⚖️ Our Expertise</span></span>
        <h2 class="section-title">Areas of <span class="colored">Practice</span></h2>
        <p class="section-subtitle">Comprehensive legal solutions with deep expertise in Indian law and judicial proceedings across all courts.</p>
      </div>

      <div class="services-grid stagger">
        <div class="service-card">
          <span class="service-number">01</span>
          <div class="service-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
          </div>
          <h3>Corporate & Commercial Law</h3>
          <p>Company formation, MOA/AOA drafting, mergers, acquisitions, regulatory compliance, and business advisory under Companies Act, 2013.</p>
        </div>

        <div class="service-card">
          <span class="service-number">02</span>
          <div class="service-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <h3>Family & Matrimonial Law</h3>
          <p>Divorce, custody, maintenance, domestic violence under DV Act, Hindu Marriage Act, Muslim Personal Law, and Special Marriage Act matters.</p>
        </div>

        <div class="service-card">
          <span class="service-number">03</span>
          <div class="service-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6"/></svg>
          </div>
          <h3>Property & Real Estate</h3>
          <p>Title verification, sale/purchase agreements, lease deeds, tenancy disputes, RERA compliance, and land acquisition matters.</p>
        </div>

        <div class="service-card">
          <span class="service-number">04</span>
          <div class="service-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 6l3 1m0 0l-3 9a5.002 5.002 0 006.001 0M6 7l3 9M6 7l6-2m6 2l3-1m-3 1l-3 9a5.002 5.002 0 006.001 0M18 7l3 9m-3-9l-6-2m0-2v2m0 16V5m0 16H9m3 0h3"/></svg>
          </div>
          <h3>Civil & Commercial Litigation</h3>
          <p>Civil suits, injunctions, recovery matters, contract disputes, arbitration, and mediation under CPC and Arbitration Act.</p>
        </div>

        <div class="service-card">
          <span class="service-number">05</span>
          <div class="service-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>
          </div>
          <h3>Criminal Defense</h3>
          <p>Bail applications, trial representation, appeals under IPC/BNS, anticipatory bail, quashing petitions under CrPC/BNSS.</p>
        </div>

        <div class="service-card">
          <span class="service-number">06</span>
          <div class="service-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
          </div>
          <h3>Legal Documentation & Advisory</h3>
          <p>Drafting of agreements, wills, POA, legal notices, pleadings, affidavits, and comprehensive legal opinions.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Team -->
  <section id="team">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag"><span>👥 Our Team</span></span>
        <h2 class="section-title">Meet Our <span class="colored">Legal Experts</span></h2>
        <p class="section-subtitle">Experienced advocates dedicated to providing exceptional legal representation and counsel.</p>
      </div>

      <div class="team-grid stagger">
        <div class="team-card">
          <div class="team-img-wrapper">
            <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=300&h=300&fit=crop&crop=face" alt="Adv. Sunil Surse" class="team-img">
            <div class="team-badge">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
            </div>
          </div>
          <h3>Adv. Sunil Surse</h3>
          <span class="role">Lead Advocate & Founder</span>
          <p>15+ years of distinguished practice in Corporate, Family, and Property law with appearances in High Court and District Courts.</p>
        </div>

        <div class="team-card">
          <div class="team-img-wrapper">
            <img src="https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=300&h=300&fit=crop&crop=face" alt="Adv. Ganesh Tombre" class="team-img">
            <div class="team-badge">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
            </div>
          </div>
          <h3>Adv. Ganesh Tombre</h3>
          <span class="role">Senior Associate</span>
          <p>Expert in Civil and Criminal litigation with extensive trial court experience across Maharashtra.</p>
        </div>

        <div class="team-card">
          <div class="team-img-wrapper">
            <img src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?w=300&h=300&fit=crop&crop=face" alt="Adv. Priya Sharma" class="team-img">
            <div class="team-badge">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
            </div>
          </div>
          <h3>Adv. Priya Sharma</h3>
          <span class="role">Family Law Specialist</span>
          <p>Dedicated practitioner handling matrimonial, custody, and domestic violence matters with compassion.</p>
        </div>

        <div class="team-card">
          <div class="team-img-wrapper">
            <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?w=300&h=300&fit=crop&crop=face" alt="Adv. Rajesh Kumar" class="team-img">
            <div class="team-badge">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
            </div>
          </div>
          <h3>Adv. Rajesh Kumar</h3>
          <span class="role">Corporate Law Expert</span>
          <p>Specializes in corporate transactions, due diligence, and regulatory compliance for businesses.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- Appointment -->
  <section id="appointment">
    <div class="container">
      <div class="appointment-wrapper">
        <div class="appointment-info reveal">
          <span class="section-tag"><span>📅 Get Started</span></span>
          <h3>Request an Initial<br><span class="colored">Consultation</span></h3>
          <p>Take the first step towards resolving your legal matters. Our experienced team is ready to understand your needs and provide the guidance you deserve.</p>

          <div class="info-item">
            <div class="info-icon">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
            </div>
            <div>
              <h4>Prompt Response</h4>
              <p>We typically respond within 24-48 hours</p>
            </div>
          </div>

          <div class="info-item">
            <div class="info-icon">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
            </div>
            <div>
              <h4>Strict Confidentiality</h4>
              <p>Your information is protected under advocate-client privilege</p>
            </div>
          </div>

          <div class="info-item">
            <div class="info-icon">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8h2a2 2 0 012 2v6a2 2 0 01-2 2h-2v4l-4-4H9a1.994 1.994 0 01-1.414-.586m0 0L11 14h4a2 2 0 002-2V6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2v4l.586-.586z"/></svg>
            </div>
            <div>
              <h4>Initial Discussion</h4>
              <p>Understand your options before formal engagement</p>
            </div>
          </div>
        </div>

        <div class="form-card reveal">
          <h3>Book Your Appointment</h3>
          <p>Fill in your details and we will get back to you shortly.</p>

          <form id="appointmentForm">
            <div class="form-grid">
              <div class="form-group">
                <label for="aName">Full Name *</label>
                <input type="text" id="aName" required placeholder="Enter your full name">
              </div>
              <div class="form-group">
                <label for="aPhone">Phone Number *</label>
                <input type="tel" id="aPhone" required placeholder="+91 XXXXXXXXXX">
              </div>
              <div class="form-group full">
                <label for="aEmail">Email Address *</label>
                <input type="email" id="aEmail" required placeholder="your@email.com">
              </div>
              <div class="form-group">
                <label for="aType">Type of Legal Matter *</label>
                <select id="aType" required>
                  <option value="">Select matter type...</option>
                  <option>Corporate / Business</option>
                  <option>Family / Matrimonial</option>
                  <option>Property / Real Estate</option>
                  <option>Civil Litigation</option>
                  <option>Criminal Defense</option>
                  <option>Documentation / Advisory</option>
                  <option>Other</option>
                </select>
              </div>
              <div class="form-group">
                <label for="aDate">Preferred Date *</label>
                <input type="date" id="aDate" required>
              </div>
              <div class="form-group full">
                <label for="aMsg">Brief Description of Your Matter</label>
                <textarea id="aMsg" placeholder="Please provide a brief overview of your legal matter..."></textarea>
              </div>
            </div>

            <div class="form-disclaimer">
              ⚠️ <strong>Important:</strong> Submitting this form does not create an advocate-client relationship. An advocate-client relationship is only established upon formal engagement as per Bar Council of India Rules.
            </div>

            <button type="submit" class="btn btn-primary form-submit">
              <span>Submit Request</span>
              <svg class="btn-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
            </button>

            <p id="appointmentStatus" class="form-status"></p>
          </form>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact -->
  <section id="contact">
    <div class="container">
      <div class="section-header reveal">
        <span class="section-tag"><span>📞 Contact Us</span></span>
        <h2 class="section-title">Get In <span class="colored">Touch</span></h2>
        <p class="section-subtitle">Reach out through any of the following channels for legal assistance.</p>
      </div>

      <div class="contact-grid stagger">
        <div class="contact-card">
          <div class="contact-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
          </div>
          <h3>Office Address</h3>
          <p>Near District Court Complex<br>Chhatrapati Sambhajinagar<br>Maharashtra - 431001</p>
        </div>

        <div class="contact-card">
          <div class="contact-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
          </div>
          <h3>Phone & Email</h3>
          <p>Phone: +91-XXXX-XXXXXX<br>Email: contact@surselawfirm.in</p>
        </div>

        <div class="contact-card">
          <div class="contact-icon">
            <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
          </div>
          <h3>Office Hours</h3>
          <p>Monday - Friday: 10:00 AM - 6:00 PM<br>Saturday: 10:00 AM - 2:00 PM<br>Sunday: Closed</p>
        </div>
      </div>

      <div class="form-card reveal" style="max-width:700px;margin:0 auto">
        <h3>Send Us a Message</h3>
        <p>Have a quick question? Drop us a message and we will respond promptly.</p>

        <form id="contactForm">
          <div class="form-grid">
            <div class="form-group">
              <label for="cName">Your Name *</label>
              <input type="text" id="cName" required placeholder="Enter your name">
            </div>
            <div class="form-group">
              <label for="cEmail">Email Address *</label>
              <input type="email" id="cEmail" required placeholder="your@email.com">
            </div>
            <div class="form-group full">
              <label for="cMsg">Your Message *</label>
              <textarea id="cMsg" rows="5" required placeholder="Type your message here..."></textarea>
            </div>
          </div>

          <div class="form-disclaimer">
            ⚠️ Messages are handled confidentially. Sending a message does not create an advocate-client relationship.
          </div>

          <button type="submit" class="btn btn-teal form-submit">
            <span>Send Message</span>
            <svg class="btn-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"/></svg>
          </button>

          <p id="contactStatus" class="form-status"></p>
        </form>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-grid">
      <div class="footer-brand">
        <h3>Surse Law Firm</h3>
        <p>Distinguished legal practice delivering professional counsel across Corporate, Family, Property, and Litigation matters with integrity and excellence. Committed to upholding justice under the laws of India.</p>
        <div class="footer-social">
          <a href="#" aria-label="LinkedIn"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg></a>
          <a href="#" aria-label="Twitter"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M23 3a10.9 10.9 0 01-3.14 1.53 4.48 4.48 0 00-7.86 3v1A10.66 10.66 0 013 4s-4 9 5 13a11.64 11.64 0 01-7 2c9 5 20 0 20-11.5a4.5 4.5 0 00-.08-.83A7.72 7.72 0 0023 3z"/></svg></a>
          <a href="#" aria-label="Facebook"><svg fill="currentColor" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 00-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 011-1h3z"/></svg></a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="#home">Home</a></li>
          <li><a href="#services">Practice Areas</a></li>
          <li><a href="#team">Our Team</a></li>
          <li><a href="#appointment">Book Consultation</a></li>
          <li><a href="#contact">Contact Us</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Practice Areas</h4>
        <ul>
          <li><a href="#services">Corporate Law</a></li>
          <li><a href="#services">Family Law</a></li>
          <li><a href="#services">Property Law</a></li>
          <li><a href="#services">Criminal Defense</a></li>
          <li><a href="#services">Civil Litigation</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Office Hours</h4>
        <ul>
          <li><a href="#">Mon-Fri: 10AM - 6PM</a></li>
          <li><a href="#">Saturday: 10AM - 2PM</a></li>
          <li><a href="#">Sunday: Closed</a></li>
          <li><a href="#">Court Holidays: Closed</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2024 Surse Law Firm. This website is for informational purposes only. | Bar Council of India Compliant</p>
      <p>Designed with ⚖️ by <span>Rohit</span></p>
    </div>
  </footer>

  <script>
    // ===== ADMIN CREDENTIALS (Change these!) =====
    const ADMIN_CREDENTIALS = {
      username: 'admin',
      password: 'surse@2024'
    };

    // ===== PRELOADER =====
    window.addEventListener('load', () => {
      setTimeout(() => {
        document.getElementById('preloader').classList.add('hide');
        setTimeout(() => {
          if (!localStorage.getItem('disclaimerAccepted')) {
            document.getElementById('disclaimerOverlay').classList.add('active');
          }
        }, 500);
      }, 2500);
    });

    // ===== DISCLAIMER FUNCTIONS =====
    function toggleAgreeButton() {
      const checkbox = document.getElementById('agreeCheck');
      const btn = document.getElementById('agreeBtn');
      btn.disabled = !checkbox.checked;
    }

    function acceptDisclaimer() {
      document.getElementById('disclaimerOverlay').classList.remove('active');
      localStorage.setItem('disclaimerAccepted', 'true');
    }

    // ===== NAVIGATION =====
    const navbar = document.getElementById('navbar');
    const menuBtn = document.getElementById('menuBtn');
    const mobileNav = document.getElementById('mobileNav');

    window.addEventListener('scroll', () => {
      navbar.classList.toggle('scrolled', window.scrollY > 50);
    });

    menuBtn.addEventListener('click', () => {
      menuBtn.classList.toggle('active');
      mobileNav.classList.toggle('active');
    });

    mobileNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        menuBtn.classList.remove('active');
        mobileNav.classList.remove('active');
      });
    });

    // ===== SCROLL REVEAL =====
    const revealElements = document.querySelectorAll('.reveal, .stagger');
    function checkReveal() {
      revealElements.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight - 100) {
          el.classList.add('active');
        }
      });
    }
    window.addEventListener('scroll', checkReveal);
    checkReveal();

    // ===== FORM HANDLERS =====
    document.getElementById('appointmentForm').addEventListener('submit', async (e) => {
      e.preventDefault();
      const status = document.getElementById('appointmentStatus');
      status.className = 'form-status loading';
      status.textContent = '⏳ Submitting your request...';

      await new Promise(r => setTimeout(r, 1500));

      const appointments = JSON.parse(localStorage.getItem('appointments') || '[]');
      appointments.push({
        id: Date.now(),
        name: document.getElementById('aName').value,
        email: document.getElementById('aEmail').value,
        phone: document.getElementById('aPhone').value,
        type: document.getElementById('aType').value,
        date: document.getElementById('aDate').value,
        message: document.getElementById('aMsg').value,
        timestamp: new Date().toISOString(),
        status: 'pending'
      });
      localStorage.setItem('appointments', JSON.stringify(appointments));

      status.className = 'form-status success';
      status.textContent = '✅ Request submitted successfully! We will contact you within 24-48 hours.';
      e.target.reset();
    });

    document.getElementById('contactForm').addEventListener('submit', async (e) => {
      e.preventDefault();
      const status = document.getElementById('contactStatus');
      status.className = 'form-status loading';
      status.textContent = '⏳ Sending your message...';

      await new Promise(r => setTimeout(r, 1500));

      status.className = 'form-status success';
      status.textContent = '✅ Message sent successfully! We will respond shortly.';
      e.target.reset();
    });

    // ===== ADMIN PANEL =====
    document.getElementById('adminLoginForm').addEventListener('submit', (e) => {
      e.preventDefault();
      const user = document.getElementById('adminUser').value;
      const pass = document.getElementById('adminPass').value;
      const status = document.getElementById('adminLoginStatus');

      if (user === ADMIN_CREDENTIALS.username && pass === ADMIN_CREDENTIALS.password) {
        document.getElementById('adminLoginCard').style.display = 'none';
        document.getElementById('adminPanel').classList.add('active');
        localStorage.setItem('adminLoggedIn', 'true');
        loadCases();
        loadAppointments();
      } else {
        status.className = 'form-status error';
        status.textContent = '❌ Invalid credentials. Please try again.';
      }
    });

    // Check if already logged in
    if (localStorage.getItem('adminLoggedIn') === 'true') {
      document.getElementById('adminLoginCard').style.display = 'none';
      document.getElementById('adminPanel').classList.add('active');
      loadCases();
      loadAppointments();
    }

    function adminLogout() {
      localStorage.removeItem('adminLoggedIn');
      document.getElementById('adminLoginCard').style.display = 'block';
      document.getElementById('adminPanel').classList.remove('active');
      document.getElementById('adminLoginForm').reset();
    }

    function switchTab(tab) {
      document.querySelectorAll('.admin-tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.admin-content').forEach(c => c.classList.remove('active'));
      event.target.classList.add('active');
      document.getElementById('tab-' + tab).classList.add('active');
    }

    // ===== CASE MANAGEMENT =====
    document.getElementById('addCaseForm').addEventListener('submit', (e) => {
      e.preventDefault();
      const status = document.getElementById('caseFormStatus');
      const cases = JSON.parse(localStorage.getItem('cases') || '[]');

      cases.push({
        id: Date.now(),
        caseNo: document.getElementById('caseNo').value,
        client: document.getElementById('caseClient').value,
        type: document.getElementById('caseType').value,
        status: document.getElementById('caseStatusSelect').value,
        court: document.getElementById('caseCourt').value,
        date: document.getElementById('caseDate').value,
        details: document.getElementById('caseDetails').value,
        createdAt: new Date().toISOString()
      });
      localStorage.setItem('cases', JSON.stringify(cases));

      status.className = 'form-status success';
      status.textContent = '✅ Case saved successfully!';
      e.target.reset();
      loadCases();

      setTimeout(() => {
        status.className = 'form-status';
      }, 3000);
    });

    function loadCases() {
      const cases = JSON.parse(localStorage.getItem('cases') || '[]');
      const container = document.getElementById('casesList');

      if (cases.length === 0) {
        container.innerHTML = '<div class="empty-state"><div class="icon">📁</div><p>No cases found. Add your first case!</p></div>';
        return;
      }

      container.innerHTML = cases.reverse().map(c => `
        <div class="case-item">
          <div class="case-info">
            <h5>${c.caseNo}</h5>
            <p><strong>Client:</strong> ${c.client}</p>
            <p><strong>Court:</strong> ${c.court || 'N/A'}</p>
            <p><strong>Details:</strong> ${c.details || 'No details provided'}</p>
            <div class="case-meta">
              <span class="case-tag ${c.status}">${c.status.charAt(0).toUpperCase() + c.status.slice(1)}</span>
              <span class="case-tag" style="background: rgba(59,130,246,0.2); color: var(--blue); border: 1px solid rgba(59,130,246,0.3);">${c.type}</span>
            </div>
          </div>
          <div class="case-actions">
            <button class="case-btn delete" onclick="deleteCase(${c.id})" title="Delete">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
            </button>
          </div>
        </div>
      `).join('');
    }

    function deleteCase(id) {
      if (confirm('Are you sure you want to delete this case?')) {
        let cases = JSON.parse(localStorage.getItem('cases') || '[]');
        cases = cases.filter(c => c.id !== id);
        localStorage.setItem('cases', JSON.stringify(cases));
        loadCases();
      }
    }

    function loadAppointments() {
      const appointments = JSON.parse(localStorage.getItem('appointments') || '[]');
      const container = document.getElementById('appointmentsList');

      if (appointments.length === 0) {
        container.innerHTML = '<div class="empty-state"><div class="icon">📅</div><p>No appointment requests yet.</p></div>';
        return;
      }

      container.innerHTML = appointments.reverse().map(a => `
        <div class="case-item">
          <div class="case-info">
            <h5>${a.name}</h5>
            <p><strong>Email:</strong> ${a.email}</p>
            <p><strong>Phone:</strong> ${a.phone}</p>
            <p><strong>Date:</strong> ${a.date}</p>
            <p><strong>Message:</strong> ${a.message || 'No message'}</p>
            <div class="case-meta">
              <span class="case-tag pending">Pending</span>
              <span class="case-tag" style="background: rgba(59,130,246,0.2); color: var(--blue); border: 1px solid rgba(59,130,246,0.3);">${a.type}</span>
            </div>
          </div>
          <div class="case-actions">
            <button class="case-btn delete" onclick="deleteAppointment(${a.id})" title="Delete">
              <svg fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"/></svg>
            </button>
          </div>
        </div>
      `).join('');
    }

    function deleteAppointment(id) {
      if (confirm('Are you sure you want to delete this appointment?')) {
        let appointments = JSON.parse(localStorage.getItem('appointments') || '[]');
        appointments = appointments.filter(a => a.id !== id);
        localStorage.setItem('appointments', JSON.stringify(appointments));
        loadAppointments();
      }
    }

    // ===== SMOOTH SCROLL =====
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
      anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });

    // ===== SET MIN DATE FOR APPOINTMENT =====
    const dateInput = document.getElementById('aDate');
    if (dateInput) {
      const today = new Date().toISOString().split('T')[0];
      dateInput.setAttribute('min', today);
    }
  </script>
</body>
</html>

# Nexcode — Instant QR Studio

A clean, single-page QR code generator built with plain HTML, CSS, and JavaScript. Turn text, links, contact info, Wi-Fi credentials, and more into a styled, downloadable QR code — no build tools, no dependencies to install.

**🔗 Live demo:** https://claude.ai/artifact/P5PeKUpRGvGk2hLK19Wn6A

![Nexcode preview](preview.png)

## Features

- **10 content types** — plain text, URL, email, phone, SMS, WhatsApp message, Wi-Fi network, contact (vCard), geolocation, and calendar event
- **Custom styling** — pick your own foreground/background colors and output size (128–512px)
- **Adjustable error correction** — L / M / Q / H levels
- **Export options** — download as PNG or SVG
- **One-click Clear** — reset the whole form instantly
- **Responsive, dark glassmorphic UI** — works on desktop and mobile
- **Zero build step** — a single `index.html` file, ready to open or deploy anywhere

## Getting Started

No installation needed.

1. Clone the repo:
   ```bash
   git clone https://github.com/BenkabaMarwa/nexcode-qr-studio.git
   ```
2. Open `index.html` in your browser.

That's it — the app runs entirely client-side.

### Deploying

Since it's a single static file, you can host it anywhere:
- **GitHub Pages** — enable Pages on this repo (Settings → Pages → deploy from `main`)
- **Netlify / Vercel** — drag and drop the folder
- Any static file host

## Tech Stack

- HTML5 / CSS3 (no framework)
- Vanilla JavaScript
- [qrcode.js](https://github.com/davidshimjs/qrcodejs) for QR generation
- Google Fonts (Poppins, Inter)

## Usage

1. Choose a **Content Type** from the dropdown.
2. Fill in the relevant fields (text, URL, Wi-Fi credentials, contact details, etc.).
3. Adjust colors, size, and error correction level as needed.
4. Click **Generate QR Code**.
5. Download your code as **PNG** or **SVG**, or hit **Clear** to start over.

## Roadmap / Ideas

- [ ] Logo embedding in the center of the QR code
- [ ] Batch generation from a CSV list
- [ ] Saved presets for colors/sizes

Contributions and suggestions are welcome — feel free to open an issue or a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

**Marwa Benkaba**
- GitHub: [@BenkabaMarwa](https://github.com/BenkabaMarwa)
- LinkedIn: [marwa-benkaba](https://www.linkedin.com/in/marwa-benkaba-916090329/)

---

© 2026 Marwa Benkaba. All rights reserved.

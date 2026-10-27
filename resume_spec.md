# Resume project: Suthan K (content is FINAL unless marked)

Goal: build a 1-page, ATS-safe master resume (.docx + PDF) plus role-wise versions.
Owner writes in Tanglish (Tamil + English). Reply in Tanglish, short and practical.
Content is FINAL and approved. Build the resume yourself only when the owner asks; he may give a sample PDF for layout only (take layout/spacing from it, NEVER its content).

## Standing rules (do not ask again)
- Must shortlist at product-based (Google/Microsoft type) and service-based companies; high ATS match; quick HR/recruiter appeal; human-sounding text (no "passionate", "results-driven", "spearheaded", "architected").
- Avoid claims that trigger unwanted interview questions. NEVER invent numbers, companies, dates or metrics. Only use facts in this file; if a number is missing, leave it out or ask.
- If a reviewer (ATS / HR / 30-year mentor) flags a claim as unproven, add a supporting detail instead of deleting it (owner explains in interviews), but no invented numbers.
- Bullets in Google XYZ style (accomplished X, measured by Y, by doing Z); qualitative outcome when no number exists.
- Skip: 2022-24 gap, degree branch, CGPA, objective, hobbies, photo, DOB, address, references, Achievements section.
- Cloudflare was used in a personal project only: Skills only, never in job bullets.
- .NET / C# stay out of Skills (used only in the IoT project; bullets still mention them).
- Current job (Magpii) gets the most space; older jobs (Comorins, Devaxcel) stay shorter. All 3 projects stay (IoT, Education, HealthTech). Must stay readable, not a dump.
- Owner removed from Skills: MongoDB, Jest, PyTest, SQS. Do not add them back.
- SQS is gone everywhere (removed from the HealthTech project line when it went to 5 skills).
- Projects show no role label and only 5 key skills each (owner's decision).

## Template (fixed; layout follows owner's sample PDF)
A4, exactly 1 page, single column, Arial, 0.6 in margins. Body 10 pt (10.5 pt overflows to 2 pages); name 20 pt bold centered; title line 10.5 pt bold navy (1F3864) centered; 2 contact lines centered; section headings bold ~13 pt, black text, thin navy bottom border: SUMMARY, SKILLS, EXPERIENCE, PROJECTS, EDUCATION (short names, not "Professional/Technical").
- Skills: each category is a bullet, category name bold.
- Job line: `Title | Company | Dates` all bold on ONE line (dates inline after a pipe, no tab, no table).
- Bullets: "•" at the margin, text indent 0.2 in (left 288 twips, hanging 288). Spacing (readable, still 1 page): line spacing 1.05 (252), paragraph spacing = base x1.2 (headings 5.4 pt before / 2.4 after, job and project lines 3 pt before, bullets 0.7 pt after). Do not go above this: next step up overflows to page 2; keep >= 1 line of slack at the bottom.
- Project line: bold project name | the 5 most important skills, on the same line, plain text. NO role (no "Full Stack Engineer"), no italic second line.
- Education: one plain line `Bachelor of Engineering (B.E.) | University College of Engineering, Nagercoil | 2019 – 2022`.
- No tables, columns, text boxes, header/footer, icons, skill bars, photo. Dates `Nov 2025 – Present`. Links without https:// (optional: make them real hyperlinks, text stays visible). File name `Suthan_K_Resume.pdf`. Clean docx metadata. Bullet font Arial (otherwise LibreOffice embeds a serif font).
- Generator used in testing: docx-js, args = out, margin twips (864 = 0.6 in), body half-points (20 = 10 pt). Verified 1 page, about 1 in blank left at the bottom.

## Header
SUTHAN K
FULL STACK DEVELOPER | SOFTWARE ENGINEER
Trivandrum, Kerala, India | +91 93843 40144 | suthanks2000@gmail.com
suthan.vercel.app | github.com/suthanks2000 | linkedin.com/in/suthan-k

## SUMMARY (LOCKED)
Full Stack Software Engineer with 2+ years of experience building client-facing web applications with React.js, Next.js, JavaScript, TypeScript, Node.js and Python. Cut API response time by 25% by optimising REST and GraphQL APIs. Hands-on with JWT/RBAC, PostgreSQL, Dockerised microservices on AWS and Azure, and CI/CD in Agile teams.

## SKILLS (LOCKED, 46 items)
- Languages: JavaScript (ES6+), TypeScript, Python, SQL
- Frontend: React.js, Next.js, Redux Toolkit, HTML5, CSS3, Tailwind CSS
- Backend & APIs: Node.js, Express.js, FastAPI, Flask, REST APIs, GraphQL, WebSockets (SignalR), Microservices
- Databases: PostgreSQL, MySQL, Redis, TimescaleDB, TypeORM, Prisma
- Cloud & DevOps: AWS (Lambda, ECS, API Gateway, S3, RDS, CloudWatch), Azure, Docker, Nginx, GitHub Actions, Cloudflare, Vercel
- Security & Testing: JWT, RBAC (role-based access control), OAuth2, Keycloak, Vitest
- Tools & Practices: Git, Jira, Agile/Scrum, Data Structures & Algorithms
(Use "REST APIs" and spell out RBAC once for ATS keyword match. If a line wraps and breaks the 1-page fit, drop "(role-based access control)" first.)
(Owner must be able to explain every skill in interviews. Remove any he did not use.)

## EXPERIENCE
**Software Engineer | Magpii Innovations | Nov 2025 – Present**
- Develop full-stack features for an Industrial IoT and Digital Twin platform and an AI-powered Education Management Platform, delivered in Agile sprints.
- Built .NET microservices with SignalR, handling 10,000+ concurrent events/sec at sub-100 ms latency.
- Built REST APIs with pagination, search and RBAC across 12+ modules of a live education platform.
- Onboard clients by turning requirements into configurations and features; resolve live production issues.

**Junior Software Developer | Comorins Technologies | Mar 2025 – Oct 2025**
- Cut manual showing coordination and booking conflicts with client self-booking and optimised scheduling logic.
- Improved SEO and load speed with server-rendered Next.js pages for an AI-powered real estate platform.
- Improved client engagement with AI-powered follow-up automation in Python; secured APIs with JWT/RBAC and shipped to Vercel via GitHub Actions CI/CD.

**Junior Software Developer | Devaxcel Tech Pvt. Ltd. | Sep 2024 – Mar 2025**
- Cut API response time by 25% by optimising GraphQL and REST APIs, and built React, TypeScript and Redux Toolkit features for a live HealthTech platform.
- Managed PostgreSQL migrations, indexing and TypeORM queries; deployed to AWS Lambda via GitHub Actions.
- Built and maintained order-related Node.js microservices in a 28-service backend, scaled independently.

## PROJECTS (header = bold name | 5 skills, no role)
**Enterprise Industrial IoT & Digital Twin Platform** | React 19, .NET 8/9, ASP.NET Core, SignalR, PostgreSQL
- Enabled real-time asset monitoring across plants with 7+ ASP.NET Core microservices and a React 19 cockpit.
- Cut multi-hop graph queries by 45% and sped up time-series aggregations 3x by combining Apache AGE and TimescaleDB in one PostgreSQL data tier.
- Cut client deployment time from 3 weeks to 2 days with a metadata-driven UI configured through JSON schemas; secured with Keycloak and tested with xUnit and Vitest (85%+ coverage).

**AI-Powered Education Management Platform** | React, Next.js, Node.js, PostgreSQL, AWS ECS
- Delivered features across 12+ modules for schools, colleges and universities, keeping data consistent across timetables, assignments and quizzes with class-wise subject integration.
- Resolved API and data compatibility issues by migrating from Prisma/MySQL to raw PostgreSQL queries.

**HealthTech App – Digital Healthcare Platform** | React, Node.js, PostgreSQL, GraphQL, AWS Lambda
- Processed 10,000+ daily orders on a live platform for medicine purchases and digital prescriptions, with staged verification.
- Automated order processing and delivery-readiness workflows with AWS Lambda, cutting manual handling.

## EDUCATION
Bachelor of Engineering (B.E.) | University College of Engineering, Nagercoil | 2019 – 2022

## Role versions (change only title line, Summary, Skills order)
Roles: Full Stack, Software Engineer (master), Backend, Node.js, Python, Frontend, React. Per JD: use exact JD words, only for skills the owner really has.
- Backend: "Backend Software Engineer with 2+ years of experience building scalable backend services and APIs with Node.js, Express.js, TypeScript and Python. Cut API response time by 25% by optimising REST and GraphQL APIs. Hands-on with JWT/RBAC, PostgreSQL, Dockerised microservices on AWS and Azure, and CI/CD in Agile teams."
- Node.js: "Node.js Developer with 2+ years of experience building scalable APIs and backend services with Node.js, Express.js, JavaScript and TypeScript, plus React.js and Next.js on the front end. Cut API response time by 25% by optimising REST and GraphQL APIs. Hands-on with JWT/RBAC, PostgreSQL, Dockerised microservices on AWS and Azure, and CI/CD in Agile teams."
- Python: "Python Developer with 2+ years of experience building backend services, APIs and AI-powered automation with Python, FastAPI and Flask, alongside Node.js and TypeScript. Cut API response time by 25% by optimising REST and GraphQL APIs. Hands-on with JWT/RBAC, PostgreSQL, Dockerised microservices on AWS and Azure, and CI/CD in Agile teams."
- Frontend: "Frontend Software Engineer with 2+ years of experience building responsive, client-facing web applications with React.js, Next.js, JavaScript and TypeScript. Cut API response time by 25% by optimising REST and GraphQL APIs. Hands-on with Redux Toolkit, Tailwind CSS, server-side rendering, JWT/RBAC and CI/CD with GitHub Actions and Vercel in Agile teams."
- React: "React Developer with 2+ years of experience building responsive, client-facing web applications with React.js, Next.js, JavaScript and TypeScript. Cut API response time by 25% by optimising REST and GraphQL APIs. Hands-on with Redux Toolkit, Tailwind CSS, Node.js APIs, JWT/RBAC and CI/CD in Agile teams."
(Role summaries are shortened to match the master; re-check each fits 1 page when building.)

## Known interview risks (owner prepares answers; do not hide in resume)
Short stints (Devaxcel 6 mo, Comorins 8 mo); 2022-24 gap; claims to explain: 10,000+ events/sec at sub-100 ms, 10,000+ daily orders, 28 microservices, 45% / 3x / 3 weeks to 2 days, 85%+ coverage, Nginx, Keycloak, OAuth2, AWS services.

## Build and check workflow
1. Generate .docx (docx npm or python-docx) from this file; export PDF with LibreOffice; save as `Suthan_K_Resume.docx/.pdf` (master) and `Suthan_K_Resume_<Role>.docx/.pdf`; keep older versions.
2. Verify: exactly 1 page (`pdfinfo`), text selectable (`pdftotext`), no tables, fonts embedded, every bullet <= 2 lines, look at the rendered page image.
3. Keyword test against a pasted JD: match %, missing keywords the owner genuinely has.
4. Review as ATS machine, HR recruiter (6-second scan), 30-year mentor; list flaws and fix them.
5. Pending (optional): real metrics for Comorins, HealthTech if the owner finds them.

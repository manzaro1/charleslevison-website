# 💰 Bricklaying Tender & Bid Preparation Skill

**Version:** 1.0  
**Budget Context:** MK 32,000,000 (Malawi Kwacha)  
**Location:** Malawi  
**Industry:** Construction / Civil Works

---

## 📋 Overview

This skill provides comprehensive tools and guidance for preparing professional brick laying tenders and bids. It covers technical proposal writing, cost estimation, compliance requirements, and document preparation specific to the Malawian construction industry.

---

## 🎯 Quick Commands

### Initialize New Tender Project
```bash
# Creates tender project structure with all templates
skill bricklaying-tender init --project-name="ProjectName" --budget=32000000 --location="Malawi"
```

### Generate BOQ from Specifications
```bash
# Creates Bill of Quantities from tender documents
skill bricklaying-tender boq --specs="path/to/specs.pdf" --output="boq.xls"
```

### Calculate Project Costs
```bash
# Estimates costs for materials, labor, and equipment
skill bricklaying-tender estimate --area=sq-meters --brick-type="common" --mortar-type="cement-sand"
```

### Compliance Check
```bash
# Validates tender against Malawian requirements
skill bricklaying-tender compliance-check --tender-doc="path/to/tender.pdf"
```

### Generate Timeline
```bash
# Creates Gantt chart and milestone plan
skill bricklaying-tender schedule --duration-weeks=12 --start-date="YYYY-MM-DD"
```

---

## 📚 Detailed Tools & Guidance

### 1. Tender Document Analysis & Requirement Extraction

#### Process Flow
1. **Document Intake** - Receive tender documents (RFP, specifications, drawings)
2. **Initial Review** - Skim for deal-breakers (eligibility, bonding, special requirements)
3. **Detailed Analysis** - Extract specific requirements
4. **Gap Analysis** - Identify missing information
5. **Compliance Matrix** - Map requirements to your capabilities

#### Key Documents to Analyze
| Document | Purpose | Key Sections |
|----------|---------|--------------|
| Instructions to Bidders (ITB) | Rules and procedures | Submission deadlines, format requirements |
| Technical Specifications | Work requirements | Materials, methods, quality standards |
| Drawings | Visual requirements | Dimensions, layouts, elevations |
| BOQ (if provided) | Quantities for pricing | Item descriptions, units, quantities |
| Conditions of Contract | Legal obligations | Payment terms, warranties, penalties |
| Eligibility Criteria | Qualification requirements | Experience, licenses, financial capacity |

#### Requirement Extraction Template
```
TENDER ANALYSIS WORKSHEET
==========================

Tender Reference: [Insert Ref]
Issuing Authority: [Client Name]
Closing Date: [Date/Time]

SECTION A: MANDATORY REQUIREMENTS
-----------------------------------
□ Bid Security/Bond required: [Amount %]
□ Registration with PPDA/MCC required
□ Tax Clearance Certificate (TPIN)
□ VAT Registration
□ Previous experience: [X] similar projects
□ Financial capacity: Bank reference required
□ Key personnel requirements: [List positions]
□ Equipment requirements: [List]

SECTION B: TECHNICAL REQUIREMENTS
----------------------------------
Brick Type: [Specify - Common, Face, Engineering, etc.]
Brick Strength: [MPa requirement]
Mortar Mix Specs: [e.g., 1:3 cement:sand]
Bond Pattern: [Stretcher, English, Flemish, etc.]
Wall Thickness: [Single/Double/225mm/230mm]
Joint Finish: [Flush, Recessed, Weathered]
Damp Proof Course: [Y/N - Material spec]
Lintels: [Type and spacing]

SECTION C: COMMERCIAL TERMS
----------------------------
Contract Duration: [Weeks]
Liquidated Damages: [% per week]
Retention: [%]
Payment Terms: [e.g., Monthly certificates]
Advance Payment: [%]

SECTION D: DOCUMENTS REQUIRED
------------------------------
□ Technical Proposal
□ Financial Proposal (Sealed separately)
□ Company Profile
□ Reference Letters
□ Financial Statements (3 years)
□ Work Plan/Methodology
□ Safety Plan
□ Environmental Management Plan
```

---

### 2. Brick Laying Cost Estimation

#### Cost Breakdown Structure for MK 32,000,000 Budget

```
TYPICAL ALLOCATION (MK 32,000,000 TOTAL)
========================================

A. MATERIALS (45-55%)                    MK 14,400,000 - 17,600,000
   ├── Bricks                              MK 6,500,000
   ├── Cement                              MK 3,200,000
   ├── Sand                                MK 2,100,000
   ├── Water                               MK 350,000
   ├── Reinforcement/DPC                    MK 800,000
   └── Contingency (10%)                   MK 1,450,000

B. LABOR (25-30%)                          MK 8,000,000 - 9,600,000
   ├── Skilled Masons                      MK 4,500,000
   ├── Unskilled Labor                     MK 2,800,000
   ├── Supervision                         MK 1,200,000
   └── Contingency (5%)                    MK 500,000

C. EQUIPMENT & TOOLS (8-10%)               MK 2,560,000 - 3,200,000
   ├── Mixing equipment                    MK 800,000
   ├── Scaffolding                         MK 1,200,000
   ├── Hand tools                          MK 450,000
   ├── Transportation                     MK 600,000
   └── Contingency (5%)                    MK 150,000

D. OVERHEADS & PROFIT (10-15%)             MK 3,200,000 - 4,800,000
   ├── Site overheads                      MK 1,200,000
   ├── Administrative costs                MK 800,000
   ├── Profit margin                       MK 2,000,000
   └── Taxes                               MK 800,000

E. CONTINGENCY (5%)                        MK 1,600,000
```

#### Material Quantities Calculations

**Brick Calculation Formula:**
```
Bricks needed = (Wall area in m² × Bricks per m²) + 5% wastage

Standard Bricks per m²:
- Single leaf (115mm): 60 bricks/m²
- Double leaf (230mm): 120 bricks/m²
- 225mm wall: 105 bricks/m²

Example: 500 m² double leaf wall
= 500 × 120 × 1.05
= 63,000 bricks
```

**Mortar Calculation:**
```
Mortar volume per m² of single leaf: 0.025 m³
Mortar volume per m² of double leaf: 0.05 m³

Cement required: 1 part
Sand required: 3 parts

For 500 m² double leaf:
= 500 × 0.05 = 25 m³ mortar
= 25 ÷ 4 = 6.25 m³ cement
= 6.25 × 1,440 kg/m³ = 9,000 kg (180 bags of 50kg)
```

**COST REFERENCE (Malawi - 2025)**
| Item | Unit | Estimated Cost (MK) |
|------|------|---------------------|
| Common bricks | 1000 units | 120,000 - 150,000 |
| Face bricks | 1000 units | 200,000 - 280,000 |
| Engineering bricks | 1000 units | 350,000 - 450,000 |
| Cement (50kg bag) | bag | 7,500 - 9,500 |
| River sand | m³ | 8,000 - 12,000 |
| Pit sand | m³ | 5,000 - 8,000 |
| Mason (skilled) | day | 8,000 - 15,000 |
| Laborer (unskilled) | day | 5,000 - 8,000 |
| Foreman/Supervisor | day | 20,000 - 35,000 |

---

### 3. Compliance Checklist for Malawi Construction Tenders

#### Legal & Regulatory Requirements

**Mandatory Registrations:**
- [ ] **PPDA Registration** - Public Procurement and Disposal of Assets
- [ ] **Malawi Revenue Authority (MRA)** - TPIN certificate valid
- [ ] **VAT Registration** - If turnover exceeds threshold
- [ ] **National Construction Industry Council (NCIC)** - If specified
- [ ] **Local Authority License** - City/District Assembly
- [ ] **Company Registration** - Registrar of Companies

**Documentation Checklist:**
- [ ] Bid Security (Bank Guarantee/Insurance Bond)
- [ ] Tax Clearance Certificate (TCC) - current year
- [ ] Original Tender Document receipt/acknowledgment
- [ ] Signed Declaration Form
- [ ] Certificate of Incorporation/Business Registration
- [ ] Audited Financial Statements (3 years)
- [ ] Bank Reference Letter
- [ ] Power of Attorney (if signing on behalf of company)

**Technical Compliance:**
- [ ] Meet minimum experience requirements (usually X similar projects)
- [ ] Key personnel CVs meet qualification criteria
- [ ] Equipment list meets specifications
- [ ] Methodology addresses all technical requirements
- [ ] Work plan matches project duration
- [ ] Health and Safety Plan included
- [ ] Environmental Management Plan (if required)

**Financial Compliance:**
- [ ] Bid within budget ceiling (if specified)
- [ ] Validity period covers evaluation period
- [ ] Currency matching (usually MK or USD)
- [ ] Arithmetic cross-check of BOQ rates
- [ ] Signature on each page of financial proposal

**Local Preference (If Applicable):**
- [ ] Citizen-owned business certificate
- [ ] Local content plan
- [ ] Staffing plan showing local employment
- [ ] Local materials utilization plan

---

### 4. Technical Proposal Writing

#### Structure Template

```
SECTION 1: COMPANY PROFILE
===========================
1.1 Company Background
    - Year established, legal status
    - Shareholding structure (especially if citizen-owned)
    - Geographical coverage and permanent staff

1.2 Experience and Track Record
    - Similar projects completed (last 5 years)
    - Client references with contact details
    - Project values and completion dates

1.3 Organizational Capacity
    - Organizational chart
    - Key permanent staff
    - Office and yard facilities

SECTION 2: UNDERSTANDING OF THE WORK
====================================
2.1 Project Scope Summary
    - Demonstrate understanding of works
    - Identify challenges and constraints
    - Quality requirements acknowledgment

2.2 Site Assessment
    - Location description
    - Access considerations
    - Environmental factors

SECTION 3: METHODOLOGY AND WORK PLAN
=====================================
3.1 Construction Methodology
    - Step-by-step approach
    - Quality control procedures
    - Material sourcing and testing

3.2 Equipment and Resources
    - Owned vs hired equipment
    - Condition and capacity
    - Backup plans

3.3 Work Schedule (Gantt Chart)
    - Critical path identification
    - Resource allocation
    - Milestone dates

SECTION 4: QUALITY ASSURANCE
=============================
4.1 Quality Control Plan
    - Inspection checkpoints
    - Testing protocols
    - Acceptance criteria

4.2 Quality Management System
    - Supervision hierarchy
    - Documentation procedures
    - Non-conformance handling

SECTION 5: HEALTH, SAFETY & ENVIRONMENT
========================================
5.1 Health and Safety Plan
    - Risk assessment
    - PPE requirements
    - Emergency procedures

5.2 Environmental Management
    - Waste management
    - Dust control
    - Site restoration

SECTION 6: KEY PERSONNEL
========================
6.1 Project Organization Chart
6.2 CVs of Key Staff
    - Project Manager
    - Site Supervisor/Foreman
    - Quality Controller

SECTION 7: ANNEXES
==================
- Company Registration
- Financial Statements
- Reference Letters
- Equipment Schedules
- Photos of Previous Work
```

#### Writing Tips
- Use active voice and specific details
- Include photos and diagrams where possible
- Reference similar completed projects
- Address all evaluation criteria explicitly
- Keep formatting professional and consistent
- Proofread thoroughly - errors suggest carelessness

---

### 5. Project Timeline & Milestone Planning

#### Standard Brickwork Project Phases

```
WEEK-BY-WEEK SCHEDULE (12-WEEK PROJECT)
=======================================

WEEK 1-2: MOBILIZATION
□ Site handover and setup
□ Establish site office
□ Install temporary services (water/power)
□ Deliver initial materials
□ Deploy first team
[MILESTONE: Site Ready for Work]

WEEK 3-4: FOUNDATION & DPC
□ Foundation brickwork
□ Damp proof course installation
□ Foundation backfilling
□ Quality inspection
[MILESTONE: Foundation Complete]

WEEK 5-8: MAIN WALL CONSTRUCTION
□ Wall construction - Phase 1 (40%)
□ Wall construction - Phase 2 (40%)
□ Opening construction (doors/windows)
□ Lintel installation
□ Wall construction - Phase 3 (20%)
□ Curing and protection
[MILESTONE: Walls Complete to Roof Level]

WEEK 9-10: FINISHING WORKS
□ Joint finishing/pointing
□ Surface cleaning
□ Minor repairs
□ Final inspection
[MILESTONE: Brickwork Substantially Complete]

WEEK 11-12: DEMOBILIZATION
□ Site cleanup
□ Remove temporary works
□ Documentation handover
□ Final acceptance
□ Project closeout
[MILESTONE: Practical Completion]
```

#### Productivity Rates (Reference)
| Activity | Unit | Daily Output per Team |
|----------|------|----------------------|
| Brick laying (walls) | m² | 8-12 m²/day |
| Brick laying (foundations) | m² | 15-20 m²/day |
| Mortar mixing | m³ | 3-5 m³/day |
| Pointing/finishing | m² | 20-30 m²/day |

**Crew Size Recommendation:**
- 1 Foreman/Supervisor (per 20 workers)
- 2 Skilled Masons
- 3 Unskilled Laborers (1 mixing, 1 carrying, 1 assisting)

---

### 6. Budget Breakdown Templates

#### Financial Proposal Format

```
BILL OF QUANTITIES - PRICING SCHEDULE
=====================================
Tender Reference: [Insert]
Project: [Project Name]
Contractor: [Your Company]
Total Bid Price: MK [Amount]

-----------------------------------------------------------------
| Item | Description | Unit | Qty | Rate (MK) | Amount (MK) |
-----------------------------------------------------------------
| A    | SITE WORKS  |      |     |           |             |
| A.1  | Site establishment | ls | 1 | 850,000 | 850,000 |
| A.2  | Site clearance | m² | 500 | 450 | 225,000 |
| A.3  | Temporary access | ls | 1 | 320,000 | 320,000 |
|      | SUBTOTAL A | | | | 1,395,000 |
-----------------------------------------------------------------
| B    | BRICK WORKS | | | | |
| B.1  | Common bricks (class 15) | 1000 | 65 | 145,000 | 9,425,000 |
| B.2  | Cement (50kg bags) | bag | 250 | 9,000 | 2,250,000 |
| B.3  | Sand (pit) | m³ | 80 | 7,500 | 600,000 |
| B.4  | Damp proof course membrane | m² | 120 | 2,500 | 300,000 |
| B.5  | Wall ties/starter bars | kg | 150 | 3,200 | 480,000 |
| B.6  | Labour - brick laying | m² | 650 | 6,500 | 4,225,000 |
| B.7  | Labour - mortar mixing | m³ | 40 | 12,000 | 480,000 |
| B.8  | Tool allowance | ls | 1 | 180,000 | 180,000 |
|      | SUBTOTAL B | | | | 17,940,000 |
-----------------------------------------------------------------
| C    | LINTELS & OPENINGS | | | | |
| C.1  | Precast concrete lintels | m | 45 | 18,000 | 810,000 |
| C.2  | Steel reinforcement lintels | kg | 800 | 3,800 | 3,040,000 |
| C.3  | Formwork | m² | 20 | 4,500 | 90,000 |
|      | SUBTOTAL C | | | | 3,940,000 |
-----------------------------------------------------------------
| D    | EQUIPMENT HIRE | | | | |
| D.1  | Concrete mixer hire (months) | month | 3 | 180,000 | 540,000 |
| D.2  | Scaffolding (lumpsum) | ls | 1 | 950,000 | 950,000 |
| D.3  | Transportation | ls | 1 | 680,000 | 680,000 |
|      | SUBTOTAL D | | | | 2,170,000 |
-----------------------------------------------------------------
| E    | OVERHEADS & PROFIT | | | | |
| E.1  | Site supervision (10%) | | | | 2,500,000 |
| E.2  | Administrative costs | ls | 1 | 950,000 | 950,000 |
| E.3  | Profit margin | % | | | 1,500,000 |
| E.4  | Contingency (5%) | | | | 1,300,000 |
|      | SUBTOTAL E | | | | 6,250,000 |
-----------------------------------------------------------------
|      | GRAND TOTAL | | | | MK 31,695,000 |
-----------------------------------------------------------------

Amount in Words: [Thirty-One Million Six Hundred Ninety-Five Thousand Malawi Kwacha Only]
```

#### Cost Summary for MK 32,000,000 Project

```
EXECUTIVE COST SUMMARY
======================
Tender: [Project Name]
Date: [Date]
Prepared by: [Name/Role]

COST ALLOCATION:
----------------
Direct Costs:                    MK 25,445,000 (79.5%)
├── Materials                    MK 14,055,000 (43.9%)
├── Labour                       MK  6,705,000 (21.0%)
└── Equipment                    MK  4,685,000 (14.6%)

Indirect Costs:                  MK  4,250,000 (13.3%)
├── Supervision                  MK  2,500,000 (7.8%)
├── Administration               MK    950,000 (3.0%)
└── Tools/Consumables            MK    800,000 (2.5%)

Contingency (5%):                MK  1,600,000 (5.0%)
Profit Margin:                   MK    705,000 (2.2%)
-----------------------------------------------
TOTAL BID PRICE:                 MK 32,000,000

RISK FACTORS:
- Material price escalation: 5-10% buffer included
- Labour availability: Rates based on current market
- Weather delays: 1 week contingency in schedule
- Quality rejects: 5% waste allowance on bricks
```

---

### 7. Sample Previous Work / Portfolio Templates

#### Project Sheet Template

```
PROJECT REFERENCE SHEET
======================

Project Name: Residential Development - [Area]
Client: [Client Name]
Contract Value: MK [Amount]
Duration: [Start] to [End] ([X] weeks)
Location: [City/District], Malawi

SCOPE OF WORK:
- [X] m² of brickwork construction
- [X] units of [type] built
- [Specific features - arches, decorative work, etc.]

KEY ACHIEVEMENTS:
✓ Completed 2 weeks ahead of schedule
✓ Zero defects at final inspection
✓ Client satisfaction score: 9/10
✓ No safety incidents recorded

CHALLENGES OVERCOME:
- Restricted site access - implemented phased delivery
- Rainy season delays - added resources to recover schedule
- Client design changes - managed variations professionally

CONTACT REFERENCE:
[Client Representative Name]
[Title]
Phone: [Number]
Email: [Email]
Permission to contact: YES / NO
```

#### Portfolio Summary Format

```
COMPANY PORTFOLIO SUMMARY
=========================

PROJECT CATEGORY: RESIDENTIAL (Last 5 Years)
--------------------------------------------
| Project | Year | Value (MK) | Status |
|---------|------|------------|--------|
| [Name] | 2024 | 18,500,000 | Complete |
| [Name] | 2023 | 28,000,000 | Complete |
| [Name] | 2023 | 15,200,000 | Complete |
| [Name] | 2022 | 22,000,000 | Complete |
| [Name] | 2021 | 12,000,000 | Complete |

PROJECT CATEGORY: COMMERCIAL / INSTITUTIONAL
--------------------------------------------
| Project | Year | Value (MK) | Status |
|---------|------|------------|--------|
| [Name] | 2024 | 45,000,000 | Complete |
| [Name] | 2022 | 35,000,000 | Complete |

TOTAL PROJECTS: [X]
TOTAL VALUE: MK [Amount]
AVERAGE PROJECT VALUE: MK [Amount]
COMPLETION RATE: [X]%

[Insert Photos - Before/During/After]
```

---

### 8. BOQ (Bill of Quantities) Preparation

#### BOQ Format Template

```
BILL OF QUANTITIES
==================

PROJECT: [Name]
LOCATION: [District], Malawi
PREPARED BY: [Your Company]
DATE: [Date]

SECTION A: PRELIMINARIES & GENERAL
-----------------------------------
A.1 Performance Bond                    [Sum]
A.2 Insurance                           [Sum]
A.3 Site Establishment                  [Sum]
A.4 Temporary Works                     [Sum]
A.5 Site Documentation                  [Sum]

SECTION B: SUBSTRUCTURE
-----------------------
B.1 Foundation excavation               [m³]
B.2 Foundation brickwork                [m²]
B.3 Damp proof course                   [m²]
B.4 Foundation backfilling              [m³]

SECTION C: SUPERSTRUCTURE - WALLS
----------------------------------
C.1 Common brick wall (115mm thick)   [m²]
C.2 Common brick wall (225mm thick)     [m²]
C.3 Face brick wall (external)          [m²]
C.4 Block wall (concrete blocks)        [m²]
C.5 Cavity wall construction            [m²]

SECTION D: OPENINGS & LINTELS
-----------------------------
D.1 Door openings                       [Nr]
D.2 Window openings                     [Nr]
D.3 Precast concrete lintels            [m]
D.4 In-situ reinforced lintels          [m]

SECTION E: FINISHES
-------------------
E.1 Joint pointing (external)           [m²]
E.2 Joint pointing (internal)           [m²]
E.3 Surface cleaning                    [m²]
E.4 Protective coating (if specified)   [m²]

MEASUREMENT NOTES:
- All brickwork measured net in m² (face area)
- Openings > 0.5m² deducted full size
- Linings/reveals measured separately
- Work above 3m height - separate rate applies
```

#### Quantity Take-Off Method

**Step 1: Calculate Wall Areas**
```
Gross Wall Area = Length × Height

Example:
Room 5m × 4m, wall height 2.8m
Perimeter = (5 + 4) × 2 = 18m
Gross Area = 18 × 2.8 = 50.4 m²

DEDUCTIONS (Openings):
Door: 0.9m × 2.1m = 1.89 m²
Window: 1.2m × 1.2m = 1.44 m²
Total deductions = 3.33 m²

NET WALL AREA = 50.4 - 3.33 = 47.07 m²
```

**Step 2: Calculate Brick Quantities**
```
For 225mm wall (double leaf):
Bricks needed = 47.07 m² × 105 bricks/m² × 1.05 (wastage)
              = 5,189 bricks
              ≈ 5,200 bricks
```

**Step 3: Calculate Mortar**
```
Mortar volume = 47.07 m² × 0.05 m³/m²
              = 2.35 m³

Cement: 2.35 ÷ 4 = 0.59 m³ = 850 kg (17 bags)
Sand: 0.59 × 3 = 1.77 m³
```

**Step 4: Calculate Labor**
```
Productivity: 10 m²/day per mason team
Days required: 47.07 ÷ 10 = 4.7 days ≈ 5 days
```

---

## 🛠️ Specialized Commands Reference

### Tender Comparison
```bash
# Compare multiple tender requirements
skill bricklaying-tender compare --tenders="tender1.pdf,tender2.pdf" --output="comparison.xls"
```

### Risk Assessment Generator
```bash
# Create project risk register
skill bricklaying-tender risk-assess --project-type="residential" --location="blantyre"
```

### Subcontractor Evaluation
```bash
# Evaluate and select subcontractors
skill bricklaying-tender subcontractor --trade="plastering" --filter="local-only"
```

### Document Generator
```bash
# Generate standard tender documents
skill bricklaying-tender generate --template="method-statement" --project="MyProject"
```

### Price Analysis
```bash
# Analyze bid competitiveness
skill bricklaying-tender price-check --my-bid="32000000" --boq="boq.xlsx"
```

---

## 📞 Support & Resources

### Important Contacts (Malawi)
| Organization | Purpose | Contact |
|--------------|---------|---------|
| PPDA | Tender regulations | www.ppda.mw |
| MRA | Tax clearance | www.mra.mw |
| NCIC | Construction standards | [Contact local office] |
| Chamber of Commerce | Business support | www.malawichamber.org |

### File Templates Location
```
workspace/
└── skills/
    └── my-custom-skill/
        └── bricklaying-tender/
            ├── templates/
            │   ├── technical-proposal-template.docx
│   ├── financial-proposal-template.xlsx
│   ├── compliance-checklist.pdf
│   ├── method-statement-template.docx
│   └── company-profile-template.pptx
└── examples/
    ├── sample-boq-completed.xlsx
    ├── sample-project-photos/
    └── sample-reference-letters/
```

---

**Version History:**
- v1.0 (2025-02-25) - Initial release for MK 32M budget context

**Last Updated:** 2025-02-25  
**Maintainer:** Construction Skill Module  
**Review Cycle:** Quarterly or when regulations change

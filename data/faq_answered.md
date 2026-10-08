# Rownd 5X Answered Customer Questions Knowledge Base

This file contains verified, officially answered customer questions for the Rownd 5X CNC machine.
AI models can consult this document to answer inbound customer inquiries.

Total answered questions: 23

---

## 1. [Launch, Pricing & Delivery] FAQ ID: 1

**Question:**
> When will Rownd 5X be available for Kickstarter / pre-order?

**Official Answer:**
Pre-orders for Rownd 5X are currently planned to begin in September. Official details will be announced together with the launch of the pre-order campaign.

---

## 2. [Launch, Pricing & Delivery] FAQ ID: 2

**Question:**
> What will be the estimated price of Rownd 5X?

**Official Answer:**
The final pricing has not been officially announced yet. Pricing details will be shared together with the launch of the pre-order campaign.

---

## 3. [Launch, Pricing & Delivery] FAQ ID: 3

**Question:**
> When will Rownd 5X shipments start?

**Official Answer:**
We are planning to begin shipping the first production units in Q2 2027.

---

## 4. [CAM, Post Processors & Programming] FAQ ID: Unassigned

**Question:**
> For Fusion 360 specifically, is the Manufacturing Extension required for simultaneous 5-axis machining with the Rownd 5X, or does Rownd provide an alternative workflow?

**Official Answer:**
The Rownd 5X will not come with its own CAM software. You will need to use a third-party CAM program to prepare your machining operations and generate the code for the machine, with the appropriate software licence obtained separately.



We are partnering with SolidCAM, and the post-processor and machine simulation work for the Rownd 5X has already been completed. The post-processor converts your programmed toolpaths into machine-specific code, while the simulation allows you to review the machining process and check for potential collisions within CAM before running it on the machine.



Fusion 360 integration is also planned, but it has not yet been completed. We will share further details as this integration progresses.

---

## 5. [CAM, Post Processors & Programming] FAQ ID: 26

**Question:**
> Will the 5x kickstarter machines include a postprocessor and simulation model for HyperMill when they ship?

**Official Answer:**
We aim to support major CAM platforms globally. We are currently developing post-processors and simulation models for SolidCAM and Fusion 360.



For other CAM software, including hyperMILL, we plan to provide the necessary machine configuration details and guidelines to support post-processor development.

---

## 6. [Machining Capacity & Materials] FAQ ID: 29

**Question:**
> What is the weight of the unit?

**Official Answer:**
The machine weighs approximately 68 kg (150 lb). The estimated shipping weight, including the protective crate, is approximately 97 kg (214 lb).

---

## 7. [Machining Capacity & Materials] FAQ ID: 32

**Question:**
> Send all spec's?

**Official Answer:**
Machine type: Fully enclosed desktop 5-axis CNC milling machine

Machining modes: 3-axis, indexed 3+2-axis, and simultaneous 5-axis

3-axis working area: 225 × 225 × 180 mm

5-axis working capacity: Approximately Ø200 × 180 mm

A-axis travel: +90° to −45°

C-axis rotation: 360°

Spindle power: 2.2 kW

Maximum spindle speed: 24,000 rpm

Spindle cooling: Liquid cooling

Tool holder: ISO20

Automatic tool changer: 10 tools

Tool cooling: Mist cooling

Machine weight: Approximately 68 kg

Linear motion: High-precision linear guides with roller carriages

Drive system: Ground ball screws with ball nuts

Target positioning repeatability: ±0.02 mm

Display: 13.3-inch touchscreen

Control system: LinuxCNC-based

Power compatibility: 110, 220 V

Total power: Approximately 2.8 kW

CAM support: SolidCAM and Autodesk Fusion, with compatibility planned for other major CAM platforms

Materials: Engineering plastics, aluminum, brass, steel, and other machinable materials

Construction: Fully enclosed cabinet with bellows and stainless-steel axis protection



The final specifications will be confirmed after the pre-production validation program. Repeatability depends on the complete motion system, including the ball screws, linear guides, preload, feedback, control tuning, structural stiffness, thermal conditions, and measurement method.

---

## 8. [Spindle & Cutting Performance] FAQ ID: Unassigned

**Question:**
> Can you provide actual aluminum roughing parameters using approximately a 6 mm or 1/4" carbide end mill, RPM, feed, axial depth of cut, radial engagement and material removal rate?

**Official Answer:**
We have carried out sustained machining tests at 5 mm axial depth, 2 mm radial engagement, 1,000 mm/min feed and 10,000 RPM. This corresponds to a nominal material removal rate of 10 cm³/min.

---

## 9. [Spindle & Cutting Performance] FAQ ID: 38

**Question:**
> Can you tell me what the usable constant-torque speed range (or VFD base frequency) for your 24,000 rpm (2-pole, I assume) spindle will be? I ask because I know your direct competitor (the upcoming Xhorse WM-100) seems to reach as low as ~1,000 rpm ,  even if effective power drops to a few hundred watts ,  so that machining titanium or low-melting-point plastics (or even tapping/reaming/boring/threading, acknowledging the limits of the form factor) isn't a problem.

**Official Answer:**
We plan to use an 800 Hz spindle motor. The final VFD settings and low-speed torque performance are still being tested. Our goal is to provide a practical speed range for titanium, engineering plastics, reaming, and boring. We will publish the verified torque and power curves once testing is complete.

---

## 10. [Cooling & Waste Management] FAQ ID: 31

**Question:**
> What is the cooling system?

**Official Answer:**
The Rownd 5X will include:



A liquid-cooled spindle

A mist cooling system for the cutting tool and workpiece

---

## 11. [Cooling & Waste Management] FAQ ID: 43

**Question:**
> How's the mist cooling waste water collection managed ?

**Official Answer:**
There is a grate underneath the A- and C-axis table that catches the chips while allowing the coolant to drain through. Under the grate, there is a sloped coolant tray where the liquid collects. The collected coolant is then drained out of the machine through a drain nozzle located at the lower side of the machine.

---

## 12. [Accuracy, Repeatability & Mechanics] FAQ ID: Unassigned

**Question:**
> How is TCP/RTCP ,  Tool Center Point compensation handled on the 5X? Is it managed directly by the machine controller? Is the kinematic calibration of the rotary axes automated or assisted?

**Official Answer:**
Yes, an automatic routine will use a calibration sphere and the optional wireless probe to measure and compensate the rotary centers and RTCP kinematics.

---

## 13. [Accuracy, Repeatability & Mechanics] FAQ ID: Unassigned

**Question:**
> What are the guaranteed XYZ positioning accuracy and repeatability, B/C rotary positioning accuracy/repeatability, and simultaneous 5-axis RTCP/tool-center-point accuracy?

**Official Answer:**
Guaranteed XYZ positioning repeatability is ±0.02 mm. Our current measured simultaneous RTCP accuracy is ±0.06 mm, with improvements ongoing. These figures are distinct from finished part tolerances, which depend on the machining conditions. Both A and C axes use Easy Servo motors with 50:1 harmonic reducers. Our tests used a collet holder with 0.005 mm runout, rather than shrink fit tooling.

---

## 14. [Accuracy, Repeatability & Mechanics] FAQ ID: 18

**Question:**
> What type of rotary drive is used for the A and C axes?

**Official Answer:**
Both A and C axes use Easy Servo motors with 50:1 harmonic reducers.

---

## 15. [Accuracy, Repeatability & Mechanics] FAQ ID: 28

**Question:**
> Repeatability seems to be 20 µm. Is that what your servos (I'd guess you're not using steppers for a value proposition like this) are limited to? When Xhorse promises 10 µm instead, are they using different measurement criteria, or could their capabilities plausibly be twice as good? Perhaps a regulatory limit?

**Official Answer:**
The ±20 µm repeatability is a conservative machine-level specification, not a limitation of the motors or encoders. Repeatability depends on the complete motion system, including the ball screws, linear guides, preload, feedback, control tuning, structural stiffness, thermal conditions, and measurement method. Testing and calibration are ongoing, so the final production specification may improve.

---

## 16. [Probing, Tool Setting & AI] FAQ ID: 34

**Question:**
> Will it have probing and AI programming?

**Official Answer:**
A workpiece probing system will be available as an optional add-on and will operate directly with the machine. It is being developed to support:



Automatic workpiece zeroing

Camera-assisted dimensional estimation

Workpiece recognition

Basic geometry detection



The AI features will be available with the first customer deliveries. Initial capabilities are planned to include:



Voice commands

Automatic zeroing

Workpiece recognition

AI-assisted G-code generation for selected operations, including pocketing, contouring, and face milling

---

## 17. [Probing, Tool Setting & AI] FAQ ID: 35

**Question:**
> Will it have tool setting?

**Official Answer:**
An automatic tool measurement probe will be included as a standard feature on every machine.

---

## 18. [Company, Testing & Media] FAQ ID: 30

**Question:**
> Who is the manufacturer of your new 5 axis unit? What experience does this company have?

**Official Answer:**
The Rownd 5X is designed and manufactured by Rownd Precision in Bursa, Türkiye.

---

## 19. [Company, Testing & Media] FAQ ID: 36

**Question:**
> How many units will be tested by pro's not in  the first phase?Second phase with makers

**Official Answer:**
Before serial production, we plan to manufacture 20 pre-production machines and subject them to different technical and durability tests.



Of these, 10 machines will be provided to selected end users for real-world testing. We will evaluate their feedback and test results, complete the necessary revisions, and then proceed to serial production.

---

## 20. [Company, Testing & Media] FAQ ID: 37

**Question:**
> What will be the option's. Do you have real trial's on video.  Thank's

**Official Answer:**
Planned options include the ATC package, wireless workpiece probe, ISO20 holder sets, cutting tool sets, vises and workholding accessories, cooling equipment, camera and machine stand. We will publish the final package contents and accessory list with the campaign.

---

## 21. [Launch, Pricing & Delivery] FAQ ID: 44

**Question:**
> If I do the VIP deal and get early ordering, can I delay my shipment?

**Official Answer:**
Yes, we can schedule shipment for your preferred date while keeping your VIP and early ordering benefits.

---

## 22. [Spindle & Cutting Performance] FAQ ID: 45

**Question:**
> What are your test results and cutting parameters for machining titanium?

**Official Answer:**
We have tested Grade 5 titanium with mist cooling and achieved good results at 0.5 mm axial depth, 0.3 mm radial engagement, 1,000 mm/min feed and 10,000 RPM. These are specific test conditions, and we are continuing to evaluate performance.

---

## 23. [Machining Capacity & Materials] FAQ ID: 46

**Question:**
> Assuming an optimal tool holder, tool length and a 55mm ID hole, is it achievable to mill down 70mm?

**Official Answer:**
Thank you for the video suggestion! We will work on testing this soon.

---


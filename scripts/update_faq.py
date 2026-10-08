import os
import re

def clean_text(text):
    return text.replace("\u2014", ", ").replace("\u2013", ", ")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    html_path = os.path.join(base_dir, "Customer Questions - Grouped.xlsm", "Grouped Questions.html")

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Update Aluminum roughing parameters
    pattern_al = r'(aluminum roughing parameters[^<]*</td><td class="s13">)(</td>)'
    rep_al = r'\1We have carried out sustained machining tests at 5 mm axial depth, 2 mm radial engagement, 1,000 mm/min feed and 10,000 RPM. This corresponds to a nominal material removal rate of 10 cm³/min.\2'
    html, count_al = re.subn(pattern_al, rep_al, html)
    print(f"Updated aluminum roughing answer: {count_al}")

    # 2. Update Kinematic calibration
    pattern_kin = r'(kinematic calibration of the rotary axes automated or assisted\?</td><td class="s16">)(</td>)'
    rep_kin = r'\1Yes, an automatic routine will use a calibration sphere and the optional wireless probe to measure and compensate the rotary centers and RTCP kinematics.\2'
    html, count_kin = re.subn(pattern_kin, rep_kin, html)
    print(f"Updated kinematic calibration answer: {count_kin}")

    # 3. Update Guaranteed XYZ accuracy and RTCP
    pattern_acc = r'(guaranteed XYZ positioning accuracy and repeatability[^<]*</td><td class="s16">)(</td>)'
    rep_acc = r'\1Guaranteed XYZ positioning repeatability is ±0.02 mm. Our current measured simultaneous RTCP accuracy is ±0.06 mm, with improvements ongoing. These figures are distinct from finished part tolerances, which depend on the machining conditions. Both A and C axes use Easy Servo motors with 50:1 harmonic reducers. Our tests used a collet holder with 0.005 mm runout, rather than shrink fit tooling.\2'
    html, count_acc = re.subn(pattern_acc, rep_acc, html)
    print(f"Updated accuracy & RTCP answer: {count_acc}")

    # 4. Update Rotary drive type (FAQ ID 18)
    pattern_rot = r'(What type of rotary drive is used for the A and C axes\?</td><td class="s16">)(</td>)'
    rep_rot = r'\1Both A and C axes use Easy Servo motors with 50:1 harmonic reducers.\2'
    html, count_rot = re.subn(pattern_rot, rep_rot, html)
    print(f"Updated rotary drive answer: {count_rot}")

    # 5. Update Options (FAQ ID 37)
    pattern_opt = r'(What will be the option&#39;s\. Do you have real trial&#39;s on video\.\s+Thank&#39;s</td><td class="s16"[^>]*>)[^<]*(</td>)'
    rep_opt = r'\1Planned options include the ATC package, wireless workpiece probe, ISO20 holder sets, cutting tool sets, vises and workholding accessories, cooling equipment, camera and machine stand. We will publish the final package contents and accessory list with the campaign.\2'
    html, count_opt = re.subn(pattern_opt, rep_opt, html)
    print(f"Updated options answer: {count_opt}")

    # 6. Add new questions before </tbody>
    new_rows = """
<tr style="height: 31px"><th class="row-headers-background"><div class="row-header-wrapper">66</div></th><td class="s10">Launch, Pricing &amp; Delivery</td><td class="s11">44</td><td class="s12">If I do the VIP deal and get early ordering, can I delay my shipment?</td><td class="s13">Yes, we can schedule shipment for your preferred date while keeping your VIP and early ordering benefits.</td><td></td></tr>
<tr style="height: 31px"><th class="row-headers-background"><div class="row-header-wrapper">67</div></th><td class="s10">Spindle &amp; Cutting Performance</td><td class="s14">45</td><td class="s15">What are your test results and cutting parameters for machining titanium?</td><td class="s16">We have tested Grade 5 titanium with mist cooling and achieved good results at 0.5 mm axial depth, 0.3 mm radial engagement, 1,000 mm/min feed and 10,000 RPM. These are specific test conditions, and we are continuing to evaluate performance.</td><td></td></tr>
<tr style="height: 31px"><th class="row-headers-background"><div class="row-header-wrapper">68</div></th><td class="s10">Machining Capacity &amp; Materials</td><td class="s11">46</td><td class="s12">Assuming an optimal tool holder, tool length and a 55mm ID hole, is it achievable to mill down 70mm?</td><td class="s13">Thank you for the video suggestion! We will work on testing this soon.</td><td></td></tr>
"""
    if 'id="1128023415R64"' in html or '</tbody>' in html:
        html = html.replace('</tbody>', new_rows.strip() + '\n</tbody>')
        print("Appended new rows to HTML table.")

    # Ensure no forbidden dashes
    html = clean_text(html)

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    print("Grouped Questions.html successfully updated.")

if __name__ == "__main__":
    main()

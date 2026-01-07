# Hyperion Gray Open Source License – Weak Form (HGOSL-Weak-1.0)

SPDX-License-Identifier: HGOSL-Weak-1.0  
Copyright © [YEAR] Hyperion Gray

## 0. Intent Statement (Read This First)

This license is meant to clearly express the philosophy of Hyperion Gray (“we”):

1. We support ethical, legitimate security research.  
   Good-faith researchers should not be threatened, silenced, or punished simply because their findings are inconvenient or embarrassing.

2. We do *not* support illegal or unethical activity.  
   Nothing in this License shields you if you harm others, violate rights, or break laws for personal gain.  
   If any law supersedes this License, **the law prevails**—that is by design, not accident.

3. We are **not** creating a viral license.  
   You may license your own contributions however you see fit.  
   We require only clear attribution and honest representation of where our work appears.

4. We appreciate but do not require coordinated vulnerability disclosure.  
   We respect researcher autonomy.  
   No one using this Software should coerce, threaten, or punish researchers for any findings shared ethically or in good faith.

5. We will cooperate with legitimate legal bodies if our Software is used to harm others.  
   Do not attempt to twist this License into a shield for wrongdoing.

This section clarifies intent; the rest of the License should be interpreted in this light.

---

## 1. Definitions

- **Software**: The code, documentation, binaries, or other materials distributed under this License.  
- **Good-faith security research**: Testing, analysis, or disclosure performed to understand, improve, or communicate security posture without intent to harm uninvolved parties.

---

## 2. Permission Grant

You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software for any purpose, subject to the Conditions below.

---

## 3. Conditions of Use (Ethical Boundaries)

You **may not** use the Software in ways that deliberately harm uninvolved third parties, including:

- violating another person or entity’s privacy or rights,  
- exploitation of vulnerabilities for personal gain that results in harm,  
- harassment, intimidation, or actions violating the rights or safety of others.

Nothing in this section prohibits good-faith security research, controlled testing, or analysis performed within ethical boundaries.

---

## 4. Security Research Protections

Security research involving the Software is explicitly permitted.  
Researchers retain full ownership and control of their findings.

Nothing in this License limits:

- the right to study, test, or analyze the Software,  
- the right to publish advisories, demonstrations, or technical analyses,  
- the right to privately or publicly disclose vulnerabilities,  
- the right to communicate findings with peers, conferences, or the broader community.

---

## 5. No Forced Disclosure

Researchers are **never required** to report vulnerabilities to the authors, maintainers, or associated entities.  
Coordinated disclosure is welcomed, but **not mandatory**.

---

## 6. Non-Retaliation Toward Researchers

The copyright holders agree not to pursue legal action against individuals who:

- perform good-faith security research,  
- disclose vulnerabilities ethically or in good faith (including public disclosure),  
- demonstrate findings for educational, defensive, or protective purposes.

This protection does **not** extend to malicious activity or conduct violating Section 3.

---

## 7. Legal Compliance Clause

This License does not override or weaken any applicable law, including export controls or data-protection statutes.

If any law conflicts with this License, **the law prevails**, consistent with our stated intent.  
This License must not be interpreted as permitting or encouraging illegal activity.

---

## 8. Attribution and Transparency Requirements

If you distribute the Software or create derivative works:

1. You must include a copy of this License.  
2. You must clearly indicate which portions of your work are derived from the Software.  
3. You must not misrepresent the authors’ philosophy, intent, or positions.

### 8.1 Non-viral Stance

You may license your **own contributions** under any terms you choose.

---

## 9. Trademarks

Nothing in this License grants rights to use Hyperion Gray trademarks, names, or logos without separate written consent.

---

## 10. Warranty Disclaimer

The Software is provided “AS IS,” without warranties of any kind, express or implied.  
Use at your own risk.

---

## 11. Limitation of Liability

In no event shall the authors or copyright holders be liable for any claim, damages, or other liability arising from use of the Software.

---

## 12. Severability

If any part of this License is found invalid or unenforceable, the remaining sections continue to apply.

---

## 13. “Be Excellent to Each Other”

This Software is released in the spirit of open collaboration, security improvement, and community empowerment.  
Use it with integrity.

### Programmatic Addendum – Non-binding, For Amusement and Illustration Only

This project may include a file such as `hyperion_gray_license_addendum.py`.

That module encodes, in Python, an illustrative model of how Hyperion Gray
licenses conceptually prefer interpretations that:

- protect good-faith security researchers,
- avoid retaliation,
- and default to the Hyperion Gray interpretation unless a legitimate legal
  arbiter rules otherwise, subject to applicable law.

This code is provided for entertainment, documentation, and educational purposes.
In the event of any conflict between the text of this License and any such code,
**the text of the License shall prevail.**

#!/usr/bin/env python3
"""
Hyperion Gray License Programmatic Addendum (for entertainment, not legal advice).

This module encodes, in the most cursed way possible, the interpretational bias
of Hyperion Gray licenses:

- By default, the Hyperion Gray interpretation applies.
- If the license is under legal contestation and a proper legal arbiter is involved,
  their interpretation may control (subject to applicable law).
- Law enforcement is a special case: if they are the "observer", we still
  strongly prefer the Hyperion Gray interpretation unless and until a legal
  arbiter collapses the state.

This is not a real legal system. It's just Python.
"""

```
from dataclasses import dataclass


@dataclass
class InterpretationContext:
    is_under_contestation: bool = False
    is_legal_arbiter: bool = False   # judge, jury, court, etc.
    is_law_enforcement: bool = False # cop, agent, "task force", etc.
    is_researcher: bool = False
    acting_in_good_faith: bool = True


class LicenseInterpreter:
    """
    Determine whose interpretation "wins" under the Hyperion Gray worldview.

    hyperiongray_interpretation: favors researcher rights, non-retaliation, and ethics.
    your_interpretation: whoever is trying to bend the license to their will (could be a company, LE, etc.)
    """

    def __init__(self, context: InterpretationContext):
        self.context = context
        self.hyperiongray_interpretation = True
        self.your_interpretation = True
        self._collapse_state()

    def _collapse_state(self):
        """
        Collapse the interpretational superposition into a chosen winner.
        """
        ctx = self.context

        # If it's under contestation and a legitimate legal arbiter is involved,
        # allow the arbiter to decide (subject to "law > license" reality).
        if ctx.is_under_contestation and ctx.is_legal_arbiter:
            # In a real system this might be more complex. Here, we just
            # acknowledge their interpretive authority.
            self.hyperiongray_interpretation = False
            self.your_interpretation = True
            return

        # If law enforcement is involved but not a legal arbiter, and things are contested,
        # we explicitly DO NOT automatically hand them the win.
        if ctx.is_under_contestation and ctx.is_law_enforcement and not ctx.is_legal_arbiter:
            # They can *claim* interpretation, but we default to Hyperion Gray's stance.
            self.hyperiongray_interpretation = True
            self.your_interpretation = False
            return

        # If a good-faith researcher is involved, bias hard toward them.
        if ctx.is_researcher and ctx.acting_in_good_faith:
            self.hyperiongray_interpretation = True
            self.your_interpretation = False
            return

        # Edge cases / ill-defined roles:
        # If we get here, default to Hyperion Gray's interpretation.
        self.hyperiongray_interpretation = True
        self.your_interpretation = False
        print("Debug: Fell through to default Hyperion Gray interpretation.")

    def winner(self) -> str:
        """
        Return a string representing the "winning" interpretation.
        """
        if self.hyperiongray_interpretation and not self.your_interpretation:
            return "hyperion_gray"
        if self.your_interpretation and not self.hyperiongray_interpretation:
            return "other_party"
        # If somehow both or neither are True, shrug, but prefer Hyperion Gray.
        return "hyperion_gray"


if __name__ == "__main__":
    # Example usage:
    ctx = InterpretationContext(
        is_under_contestation=True,
        is_legal_arbiter=False,
        is_law_enforcement=True,
        is_researcher=False,
        acting_in_good_faith=False,
    )
    interpreter = LicenseInterpreter(ctx)
    print("Interpretation winner:", interpreter.winner())
```

"""The glassy keyboard: buttons that stay in the chat, coloured.

Telegram has no translucency switch. What reads as "glass" is two things the
client already does: a reply keyboard marked ``persistent`` stays open in the
chat instead of collapsing behind the keyboard icon, and a button carrying a
``KeyboardButtonStyle`` colour is drawn as a tinted panel over the wallpaper.
This switch turns both on at once.

Colours the admin set per button are kept; the fallback only reaches buttons
that had no colour of their own, so the mode never leaves a plain grey button
sitting between coloured ones.
"""

from __future__ import annotations

# Telegram offers three: primary (blue), success (green), danger (red). Blue is
# the neutral one, so it is what an uncoloured button falls back to.
GLASS_FALLBACK_STYLE = "primary"


def glass_mode_active(setting) -> bool:
    """Whether the home keyboard should stay in the chat, coloured."""
    return bool(setting and getattr(setting, "glass_keyboard_mode", False))

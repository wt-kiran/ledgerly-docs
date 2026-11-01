# First setup and signing in

The first-run page appears only while the installation has no login users. It creates the initial real household and owner account. New households start without another household's transactions, goals or plan.

## Create the first household

1. Enter a household name, such as **Example Household**.
2. List financial members, one per line or separated by commas. For example, Alex and Jamie. Blank names and repeated names are removed at creation.
3. Choose the first owner's username and optional display name.
4. Enter a password of at least 12 characters and enter it again in Confirm password.
5. Select **Create household**. Ledgerly signs you into Overview.

## Fields and choices

| Field | Defaults, required values and validation | What changes |
|---|---|---|
| Household name | Required, stripped, nonempty; unique case-insensitively among household names | Renames primary household registry record |
| Household financial members | Required; at least one; comma/newline separated; stripped; blank entries removed and duplicate casefold names removed | Creates people whose finances are modelled; not login accounts |
| Administrator username | Required, stripped; unique case-insensitive | Creates local login and owner membership |
| Display name | Optional in setup, falls back to username | Name shown for login user, independent of financial members |
| Password | Required, at least 12 characters | Hashed PBKDF2 SHA256 with 600000 iterations |
| Confirm password | Required and must match password | Checks correct password entry |

Use memorable household labels rather than sensitive account details. Financial member names identify ownership and responsibility; creating one does not create a sign-in account.

## Sign in to an existing installation

Enter your username and password and select a household you have access to. The household list contains active real households; membership is checked during sign-in. Usernames are matched without case sensitivity. Household names are visible on the login page, so do not use confidential labels.

## Fields and choices

| Field | Defaults, required values and validation | What changes |
|---|---|---|
| Username | Required, stripped, case-insensitive lookup of active user | Selects local user |
| Password | Required, matched to password hash | Authenticates locally |
| Household | Required browser selection; defaults to first alphabetically listed non-demo active household | User must have membership in chosen household |

Five failed attempts from the same client address within 15 minutes temporarily block more attempts. The signed-in session lasts up to eight hours. **Sign out** clears the session; closing a browser tab alone is not a sign-out operation.

## Add another user later

An Owner or Admin can open **Households** and use **Create user**. Select the appropriate household checkboxes; a new user starts as Member in those allowed households. [Household management](../guide/households.md) explains the current permission limitations.

## Password and session problems

There is no email reset or web password-change page. Ask the installation administrator for [support-assisted local recovery](../troubleshooting.md#login-and-password-problems). Do not rerun first setup or delete the database to reset a password.

If a form reports an invalid/expired token, refresh the page, sign in again if needed, and re-enter the change. A security token is added by Ledgerly; it is not a setting you choose.

**Example:** Alex is the login user who maintains the household. Alex and Jamie are both financial members; Jamie does not need a separate login unless they also need to use Ledgerly.

Related: [Demo Mode](../guide/demo.md), [FAQ](../faq.md), [privacy](../privacy.md).

# Households, members and login users

Use **Households** for separate financial records, member names and user access. A **financial member** is part of the model; a **login user** is an account allowed to sign in. They are separate lists and need not contain the same people.

## Roles and actual permissions

| Role | What v3.8.5 actually enforces |
|---|---|
| Owner | Can use Households/access management; may delete an eligible isolated household |
| Admin | Can use Households/access management; cannot use the owner-only household deletion action |
| Member | Can use financial screens; cannot open Households administration |
| Viewer | Cannot open Households administration, but **is not read-only** on financial screens |

!!! warning "Use only with trusted login users"
    Viewer can make financial changes. There is also a startup limitation that can grant an existing login Owner membership in the primary household when that membership is missing. Separate files do not guarantee separate access for untrusted users. Do not use roles or household separation as a strong privacy boundary in this release.

There is no configured numerical cap on households, login users or financial members, but this is not a scalability/tested-capacity guarantee. Each household needs at least one active financial member. Demo does not offer this administration screen.

## Create or switch household

An Owner/Admin opens Households, enters a unique household name and at least one member, then selects **Create household**. Member names can be comma/newline separated; repeated names are removed at creation. No transactions, goals, tax scenarios or Plan are copied into the new household. The creator becomes its Owner.

When more than one allowed real household is available, use the sidebar selector to switch. Confirm the active household name before importing or changing a plan. A household is not a new software installation.

## Manage financial members

Use **Add member** or rename the relevant member. **Remove** deactivates the person. If they own accounts or have recurring/goal/allocation responsibility, choose another active member to receive those records first. The household must retain at least one member. Responsibility follows the reassignment; changing a name does not create a login or transfer money.

## Create a login and set access

Enter display name, unique username, a password of at least 12 characters, and one or more household-access checkboxes. Select **Create user**. Allowed memberships are initially Member; use **Save access** to change a role later. Owners/Admins can assign the listed roles, including Owner. There is no built-in last-owner protection—avoid removing your only administrative access.

## Fields and choices

| Field | Defaults, required values and validation | What changes |
|---|---|---|
| Household name / Member name | Create household requires stripped nonempty household name; member add/rename require nonempty unique name in household | Creates household or adds/renames financial member according to action |
| Financial members | At least one; comma/newline splitting, strips and de-duplicates case-insensitively at household creation | Creates financial-member people in new isolated household |
| Display name | HTML required for create user; server falls back to username | Display label for login user |
| Username | Required, stripped; unique case-insensitive | Creates active local user |
| Password | Required at least 12 characters | Creates local password hash |
| Household access checkboxes | At least one posted value; memberships added only for households current user owns/admins | New user receives member role in selected allowed households |
| Reassign records to / Remove only if unused | Optional; must be another active person in same household when used | Moves account ownership, recurring/goal/allocation responsibility and variable scope before deactivation |
| Access role | owner/admin/member/viewer; defaults member; invalid role a rejected form | Creates or updates membership |
| Type household name to confirm | Required exact case-sensitive matching name | Enables permanent deletion of nonprimary household |

## Delete a household carefully

Only an Owner can permanently delete an eligible non-primary household. Type its name exactly as confirmation. Deletion removes its isolated financial database and membership records. It has no UI undo. The primary household cannot be deleted because its database also holds the login/household registry.

Make an independent backup first if records matter. Do not delete a household merely to fix a login or import problem. There is no household rename, login disable/delete, access-revoke or password-reset control in this web screen. Ask support for installation-level administration rather than inventing a database repair.

**Example:** Alex maintains two trusted-family household models but only one login. Jamie can be a financial member in either without a login. If Jamie needs to use the application, create a login separately and understand the early-release access limitations above.

Related: [setup](../getting-started/setup.md), [privacy](../privacy.md), [FAQ](../faq.md), [household troubleshooting](../troubleshooting.md#household-and-member-problems).

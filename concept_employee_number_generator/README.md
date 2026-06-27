# Employee Number Generator

Automatically assign unique, sequential employee numbers to HR records in Odoo 17 using a single-click action or list view bulk operations.

## Key Features

- **One-Click ID Generation**: Assign a unique employee number dynamically from the employee form view header.
- **Bulk Action Support**: Generate sequential numbers for multiple employees at once via the Actions menu in the list view.
- **Searchable ID Numbers**: Search for employees using the generated employee number in the standard search filter.
- **Custom Sequence Formats**: Fully customize the prefix (e.g. `EMP-`), padding (e.g. `00000`), and next number using Odoo's native Sequences.
- **Safe Execution**: Automatically skips records that already have an assigned employee number to prevent accidental overwrites.

## Module Structure

- `data/`: Sequence configuration (`employee_number_sequence.xml`) and list view bulk action (`employee_bulk_action.xml`).
- `models/`: Custom business logic inheriting `hr.employee` to generate the sequence values.
- `static/description/`: Main App Store cover banner, custom HTML landing page, screenshots, and Concept Solutions corporate assets.
- `views/`: Layout changes adding the "Generate Employee Number" button and sequence fields to the employee views.

## Installation

1. Copy the `concept_employee_number_generator` folder into your Odoo custom addons directory.
2. Update the Odoo Apps list.
3. Install **Employee Number Generator**.
4. Configure your prefix/padding under **Settings > Technical > Sequences** by editing the sequence named *Employee Number*.

## License

This module is licensed under the **LGPL-3** license. Developed by [Concept Solutions](https://www.csloman.com).

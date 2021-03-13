## `get`
::: pyskroutz.flags.get
    rendering:
      show_root_toc_entry: false

**Example**

=== "Request"

    ```python
    pyskroutz.flags(client).get().execute()
    ```

=== "Response (pydantic object)"

    ```python
    FlagList(
        flags=[
            FlagBaseItem(reason="bad_language", description="Περιέχει απρεπείς εκφράσεις"),
            FlagBaseItem(reason="wrong_section", description="Περιέχει ερώτηση/συζήτηση"),
            FlagBaseItem(reason="spam", description="Περιέχει παραπλανητικές πληροφορίες"),
        ]
    )
    ```

## Response Models
::: pyskroutz.models.flags
    rendering:
      show_root_heading: false
      show_root_toc_entry: false
      heading_level: 3
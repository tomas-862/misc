
# Advanced Regex Guide for Network Engineers

Enhance your network engineering toolkit with these regex examples. This guide expands into BGP configurations and IP address extraction.

## Special Characters Recap

- `.` : Matches any character except newline.
- `\d` : Matches any digit.
- `\w` : Matches any word character.
- `\s` : Matches any whitespace.

## Anchors Recap

- `^` : Start of a string.
- `$` : End of a string.
- `\b` : Word boundary.

## Quantifiers Recap

- `*` : Zero or more times.
- `+` : One or more times.
- `?` : Zero or one time.
- `{n}` : Exactly `n` times.
- `{n,}` : `n` or more times.
- `{n,m}` : Between `n` and `m` times.

## IP Address Matching

- **IPv4 Address**: `\b(?:\d{1,3}\.){3}\d{1,3}\b`
  - Matches IPv4 addresses like `192.168.1.1`.
  - Use non-capturing groups `(?:...)` for better performance.

## BGP Configuration Examples

- **BGP AS Number**: `bgp\s+([0-9]+)`
  - Matches BGP AS numbers in configurations, such as `bgp 64512`.
  - `\s+` matches whitespace between 'bgp' and the AS number.

- **Neighbor IP**: `neighbor\s+((?:\d{1,3}\.){3}\d{1,3})`
  - Captures the neighbor IP address in a BGP configuration line like `neighbor 192.168.0.1`.
  - Use `()` for capturing the actual IP address from the text.

- **Route Map Extraction**: `route-map\s+(\S+)`
  - Extracts the name of a route-map configuration, such as `route-map CUSTOM-POLICY`.
  - `\S+` matches any non-whitespace characters following 'route-map'.

## More Examples

- **Selecting Lines in Log Files**: `^(.*error.*|.*fail.*)$`
  - Matches any lines in logs containing "error"

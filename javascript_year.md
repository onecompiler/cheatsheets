# JavaScript Code for Automate Year Change

## _JavaScript dates_

## Definition and Usage

- `getFullYear()` this function return full year in 4 digit like (2022).

```sh
<!DOCTYPE html>
<html>
<body>
<h2>Copyright <span id="year_demo"> </span> by your company name. All Rights Reserved</h2>
<script>
const d = new Date();
let year = d.getFullYear();
document.getElementById("year_demo").innerHTML = year;
</script>
</body>
</html>
```

## Here is output

```
Copyright 2022 by your company name. All Rights Reserved
```

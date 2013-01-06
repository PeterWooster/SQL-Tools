one;two;three;
this isn't really sql it's just a test of the splitter;
note that the previous line had a quoted string in it; this has a ";" in quotes;
that should not be treated -- as end of line, this is a single line comment
and then /* there are multi line comments
that must be treated properly */ and allowed to span lines;
and; of course; multiple ";"s should work; properly;and one more;
before we end `;with` an unclosed statement
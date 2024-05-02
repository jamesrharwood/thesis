-- counts words in a document

words = 0
characters = 0
characters_and_spaces = 0
process_anyway = false
tables = 0
figures = 0
citations = 0
table_words = 0
citation_words = 0
references_words = 0
appendix_words = 0
div = 0
divs = 0

table_wordcount = {
  Str = function(el)
    -- we don't count a word if it's entirely punctuation:
    if el.text:match("%P") then
        table_words = table_words + 1
    end
  end,
}

references_wordcount = {
  Str = function(el)
    -- we don't count a word if it's entirely punctuation:
    if el.text:match("%P") then
        references_words = references_words + 1
    end
  end,  
}

citation_wordcount = {
  Str = function(el)
    -- we don't count a word if it's entirely punctuation:
    if el.text:match("%P") then
        citation_words = citation_words + 1
    end
  end,  
}

wordcount = {
  Str = function(el)
    -- we don't count a word if it's entirely punctuation:
    if el.text:match("%P") then
        words = words + 1
    end
    characters = characters + utf8.len(el.text)
    characters_and_spaces = characters_and_spaces + utf8.len(el.text)
  end,

  Space = function(el)
    characters_and_spaces = characters_and_spaces + 1
  end,

  Code = function(el)
    _,n = el.text:gsub("%S+","")
    words = words + n
    text_nospace = el.text:gsub("%s", "")
    characters = characters + utf8.len(text_nospace)
    characters_and_spaces = characters_and_spaces + utf8.len(el.text)
  end,

  CodeBlock = function(el)
    _,n = el.text:gsub("%S+","")
    words = words + n
    text_nospace = el.text:gsub("%s", "")
    characters = characters + utf8.len(text_nospace)
    characters_and_spaces = characters_and_spaces + utf8.len(el.text)
  end,

  Table = function(el)
    tables = tables + 1
    pandoc.walk_block(pandoc.Div(el), table_wordcount)
  end,

  Image = function(el)
    figures = figures + 1
  end,

  Cite = function(el)
    citations = citations + 1
    pandoc.walk_block(pandoc.Div(el), citation_wordcount)
  end,
}

-- check if the `wordcount` variable is set to `process-anyway`
function Meta(meta)
  if meta.wordcount and (meta.wordcount=="process-anyway"
    or meta.wordcount=="process" or meta.wordcount=="convert") then
      process_anyway = true
  end
end

function Pandoc(el)
    -- skip metadata, just count body:
    -- pandoc.walk_block(pandoc.Div(el.blocks), replaceTables)
    pandoc.walk_block(pandoc.Div(el.blocks), wordcount)
    references = pandoc.utils.references(el)
    pandoc.walk_block(pandoc.Div(references), references_wordcount)
    print(words)
    print(table_words)
    print(tables)
    print(figures)
    if not process_anyway then
      os.exit(0)
    end
end
pattern = "#%a"
return {
    {
      Para = function (elem)
        if FORMAT:match 'html' then
          if (elem.content[1].text ~= nil and elem.content[1].text:find(pattern) ~= nil) then
            elem.content[1].text = elem.content[1].text:sub(2)
            text = pandoc.utils.stringify(elem)
            text = '<div class="page-columns page-full"><p></p><div class="no-row-height column-margin column-container"><span class="">'.. text ..'</span></div></div>'
            return pandoc.RawBlock("html", text)
          else
            return elem
          end
        end
      end,
    }
  }


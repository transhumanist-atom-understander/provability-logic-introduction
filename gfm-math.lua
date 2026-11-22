-- GitHub applies Markdown backslash escapes inside $$...$$, so \\ arrives
-- as \ and multi-line math breaks. A ```math block is left verbatim, so
-- display math is written as one, splitting any paragraph around it.
function Para(el)
  local blocks, inlines = {}, {}
  local function flush()
    while #inlines > 0 and (inlines[#inlines].t == 'SoftBreak'
        or inlines[#inlines].t == 'Space') do
      table.remove(inlines)
    end
    if #inlines > 0 then
      table.insert(blocks, pandoc.Para(inlines))
    end
    inlines = {}
  end
  for _, x in ipairs(el.content) do
    if x.t == 'Math' and x.mathtype == 'DisplayMath' then
      flush()
      local text = x.text:gsub('^%s+', ''):gsub('%s+$', '')
      table.insert(blocks, pandoc.RawBlock('markdown', '```math\n' .. text .. '\n```'))
    elseif not (#inlines == 0 and (x.t == 'SoftBreak' or x.t == 'Space')) then
      table.insert(inlines, x)
    end
  end
  flush()
  return blocks
end

from lxml import etree


#Paste your xml text here
xml_data = """ 
<agency>
    <bride bid="11" name="A">
        <city>C1</city>
        </bride>
    <groom gid="33" name="C">
        <city>C1</city>
        <hobby>video games</hobby>
    </groom>
    <interest bid="11" gid="33" >
        <date>Nov 1</date>
        <rating>9</rating>
    </interest>
    <interest bid="22" gid="33">
        <rating>8</rating>
    </interest>
    <bride bid="22" name="B">
        <hobby>sport</hobby>
    </bride>
    <interest gid="33" bid="11" ggg="6">
        <date>Feb 13</date>
        <rating>10</rating>
    </interest >
</agency>
"""

# Parsing XML
root = etree.fromstring(xml_data)


####################################
#      Example queries xpath
####################################
# XPath Query: Select grades > 90
#grades = root.xpath("//student[grade > 90]/grade/text()")
#grades = root.xpath("//cake[level>3]/id(@ingredients)/attribute::name")
#grades = root.xpath("//articles[id(@pname)/country/text()='Portugal']/@aname")
#grades = root.xpath("//*/@*")
#grades = root.xpath("/descendant::name/ancestor::*")
#grades = root.xpath("/descendant::name[ancestor::student]")
grades = root.xpath("/descendant::*[attribute::ggg]/preceding-sibling::*")
#####################################


#Processing end printing result
new_root = etree.Element("result")
print('#'*35)
print(f'{len(grades)} results was founded in xml')
if len(grades) > 0 and len(str(grades[0])) > 10 :#If-else because the result might be a short attribute or a long XML element
    for i in  grades:
        new_root.append(i)
        print(etree.tostring(new_root, pretty_print=True, encoding="unicode"))
        new_root.clear()
        print('*'*35)

#    print(etree.tostring(new_root, pretty_print=True, encoding="unicode"))
else:
    print(grades)


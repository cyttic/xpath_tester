from lxml import etree

class xml_process():
#Paste your xml text here
    def __init__(self):
        self.xml_data = """ 
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

    def parsing(self, xpath_que):
    # Parsing XML
        root = etree.fromstring(self.xml_data)
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
        #grades = root.xpath("/descendant::*[attribute::ggg]/preceding-sibling::*")
        #####################################
        self.grades = root.xpath(xpath_que)

        #Processing end printing result
        new_root = etree.Element("result")
        result = []
        result.append('#'*35)
        result.append(f'{len(grades)} results was founded in xml')
        if len(grades) > 0 and len(str(grades[0])) > 10 :#If-else because the result might be a short attribute or a long XML element
            for i in  grades:
                new_root.append(i)
                result.append(etree.tostring(new_root, pretty_print=True, encoding="unicode"))
                new_root.clear()
                append('*'*35)

        #print(etree.tostring(new_root, pretty_print=True, encoding="unicode"))
        else:
            append(grades)


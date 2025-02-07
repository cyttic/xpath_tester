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
    def setTextxml(self,xml_new):
        self.xml_data = xml_new

    def parsing(self, xpath_que):
    # Parsing XML
        try:
            root = etree.fromstring(self.xml_data)
        except Exception as e:
            return 'Some error in the xml'
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
        try:
            self.grades = root.xpath(xpath_que)
        except Exception as e:
            return 'Error in the xpath'

        #Processing end printing result
        new_root = etree.Element("result")
        result = []
        result.append(f'{"#"*5} {len(self.grades)} results was founded in xml {"#"*5}\n')
        if len(self.grades) > 0 and len(str(self.grades[0])) > 10 :#If-else because the result might be a short attribute or a long XML element
            for i in  self.grades:
                new_root.append(i)
                result.append(etree.tostring(new_root, pretty_print=True, encoding="unicode"))
                new_root.clear()
                result.append('*'*20)
            return ''.join(result)
        else:
            return ' '.join(self.grades)


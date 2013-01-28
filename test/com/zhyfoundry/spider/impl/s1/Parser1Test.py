from com.zhyfoundry.spider.impl.s1 import Parser1
import unittest

class Parser1Test(unittest.TestCase):

    def testParse(self):
        c = Parser1.Parser1()

        parseResult = c.parse("""<tr><td><div><a href="/test.html?action=profile&cid=1" name="1">test1</a></div><div><a href="/test.html?action=profile&cid=2" name="2">test2</a></div></td></tr>""", "http://www.zhyfoundry.com/")
        self.assertEqual(None, parseResult.content)
        self.assertTrue(len(parseResult.newSeeds) == 2)

        parseResult2 = c.parse("""

<TABLE CLASS=bodycopy>
    <TBODY>
        <TR>
            <TD>
                <table>
                    <tbody>
                        <tr>
                            <td width="50">&nbsp;</td>
                            <td class="bold">Enterprise Name</td>
                        </tr>
                        <tr>
                            <td width="50">&nbsp;</td>
                            <td>aaa<br>bbb<br>ccc<br>ddd<br></td>
                        </tr>
                        <tr>
                            <td width="50">&nbsp;</td>
                            <td>Company Address</td>
                        </tr>
                        <tr>
                            <td align="right" width="50">&nbsp;</td>
                            <td>&nbsp;</td>
                        </tr>
                        <tr>
                            <td align="right" width="50">&nbsp;</td>
                            <td>&nbsp;</td>
                        </tr>
                        <tr>
                            <td align="right" width="50">Tel:</td>
                            <td>123456</td>
                        </tr>
                        <tr>
                            <td align="right" width="50">Fax:</td>
                            <td>234567</td>
                        </tr>
                        <tr>
                            <td align="right" height="40" width="50">Email:</td>
                            <td><a href="mailto:test@zhyfoundry.com">test@zhyfoundry.com</a></td>
                        </tr>
                        <tr>
                            <td align="right" width="50">Web:</td>
                            <td><a href="http://www.zhyfoundry.com/" target="_blank">www.zhyfoundry.com</a></td>
                        </tr>
                    </tbody>
                </table>
                <p>
            </TD>
        </TR>
    </TBODY>
</TABLE>


        """, "http://www.zhyfoundry.com/")
        self.assertEqual('Enterprise Name', parseResult2.content.name)
        self.assertEqual('test@zhyfoundry.com', parseResult2.content.email)
        self.assertEqual('123456', parseResult2.content.tel)
        self.assertEqual('234567', parseResult2.content.faxNo)
        self.assertEqual('www.zhyfoundry.com', parseResult2.content.source)
        self.assertEqual('aaa bbb ccc ddd', parseResult2.content.keyword)

        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
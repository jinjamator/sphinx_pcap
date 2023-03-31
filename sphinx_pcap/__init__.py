import sys
import os
from docutils.parsers.rst import Directive, directives
from docutils import nodes

__version__=0.1

class PCAP(Directive):
    required_arguments = 0
    optional_arguments = 4
    has_content = False

    option_spec = {
        'linenos': directives.flag,
        'output_language': directives.unchanged,  # needed for pygments lexer on output data
        'filename': directives.path,
        'tshark_path': directives.path,
        'frames': directives.unchanged,
        'filter': directives.unchanged,

    }

    
    def get_frame_filter(self,filter_string):
        r = []
        for i in filter_string.split(','):
            if '-' not in i:
                r.append(int(i))
            else:
                l,h = map(int, i.split('-'))
                r+= range(l,h+1)
        retval="or ".join(r)
        return f"({retval})"


    
    def run(self):
        output_language = self.options.get('output_language') or 'none'
        filename = self.options.get('filename')
        tshark_path = self.options.get('tshark_path') or '/usr/bin/tshark'
        _frame_display_filter=""
        if self.options.get('frames'):
            _frame_display_filter=self.get_frame_filter()
        

        # display_filter = self.options.get('display_filter') or ''
        _cli=[tshark_path,'-r',filename,'-V',]



def setup(app):
    """ Register directive with Sphinx """
    app.add_directive('include_pcap', PCAP)
    return {'version': __version__}

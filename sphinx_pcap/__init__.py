import sys
import os
from docutils.parsers.rst import Directive, directives
from docutils import nodes

__version__=0.1

class PCAP(Directive):
    required_arguments = 0
    optional_arguments = 3
    has_content = False
    
    option_spec = {
        'linenos': directives.flag,
        'output_language': directives.unchanged,  # needed for pygments lexer on output data
        'filename': directives.path,
    }

    
    def run(self):
        output_language = self.options.get('output_language') or 'none'
        filename = self.options.get('filename')




def setup(app):
    """ Register directive with Sphinx """
    app.add_directive('include_pcap', PCAP)
    return {'version': __version__}

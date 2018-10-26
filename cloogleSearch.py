import sublime
import sublime_plugin

from .cloogle import request

class CloogleSearchCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.erase_phantoms("cloogle")
		selections = self.view.selection
		if not selections:
			return

		selection = self.view.substr(selections[0])
		if not selection:
			return

		resp = request(selection)
		if resp.retrn == 0 or resp.retrn == 1:
			hit = resp.data[0]
			hrepr = hit.representation()
			hrepr = hrepr.replace("\n", "<br>")
			print(hrepr)
			self.view.add_phantom("cloogle", selections[0], "<a href=\"close\">Close</a><br><b>Cloogle: </b><pre>"+ hrepr+"</pre><", sublime.LAYOUT_BLOCK, self.on_navigate)
		elif resp.retrn >= 127 or resp.retrn <= 130:
			print("No results")

	def on_navigate(self, link):
		self.view.erase_phantoms("cloogle")
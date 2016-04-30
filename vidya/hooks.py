# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "vidya"
app_title = "Vidya"
app_publisher = "Frappe"
app_description = "Open Source AIML Bot"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@frappe.io"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vidya/css/vidya.css"
# app_include_js = "/assets/vidya/js/vidya.js"

# include js, css files in header of web template
# web_include_css = "/assets/vidya/css/vidya.css"
# web_include_js = "/assets/vidya/js/vidya.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "home"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "vidya.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "vidya.install.before_install"
# after_install = "vidya.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vidya.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"vidya.tasks.all"
# 	],
# 	"daily": [
# 		"vidya.tasks.daily"
# 	],
# 	"hourly": [
# 		"vidya.tasks.hourly"
# 	],
# 	"weekly": [
# 		"vidya.tasks.weekly"
# 	]
# 	"monthly": [
# 		"vidya.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "vidya.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vidya.event.get_events"
# }


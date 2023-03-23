"""
The `views` package contains Flask view functions for handling HTTP requests.

The following modules are included:
    - `auth`: defines view functions for user authentication.
    - `site`: defines view functions for rendering site pages.
    - `teams`: defines view functions for rendering pages related to teams.
    - `profile`: defines view functions for rendering and updating user profiles.
    - `invites`: defines view functions related to game & team invitations.

See the respective modules for detailed information on each view function and its expected input and output.
"""
from web.views.auth import *
from web.views.site import *
from web.views.teams import *
from web.views.profile import *
from web.views.invites import *
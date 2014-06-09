### Session Management
-----

* Create a new tmux session named *session_name*
```
tmux new -s session_name
```

* List existing tmux sessions
```
tmux ls
tmux list-sessions
```

* Attach to an existing tmux session named *session_name*
```
tmux attach -t session_name
```

* Switch to an existing session named *session_name*
```
tmux switch -t session_name
```

* Detach from the currently attached session
```
tmux detach
<prefix> + d
```

### External Links
-----
* http://robots.thoughtbot.com/a-tmux-crash-course
* https://wiki.archlinux.org/index.php/tmux

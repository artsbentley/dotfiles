if status is-interactive
    # Commands to run in interactive sessions can go here
end

if status is-interactive
    # Commands to run in interactive sessions can go here
end

#ALIASES
alias cls='clear'
alias df='df -h'                          # human-readable sizes
alias free='free -m'                      # show sizes in MB
alias np='nano -w PKGBUILD'
alias more=less
alias ..='cd ..'
alias cp='cp -i'
alias mv='mv -i'
alias rm='rm -i'
alias ls='exa -al --color=always --group-directories-first'
alias la='exa -a --color=always --group-directories-first'
alias ll='exa -l --color=always --group-directories-first'
alias lt='exa -aT --color=always --group-directories-first'
alias l.='exa -a | egrep "^\."'
alias cat='bat'
alias pacsyu='sudo pacman -Syu'
alias vim='nvim'

#STARSHIP PROMPT
starship init fish | source

#NEOFETCH
neofetch

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
# eval /home/martin/anaconda3/bin/conda "shell.fish" "hook" $argv | source
# <<< conda initialize <<<


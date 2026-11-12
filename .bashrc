pkill -f "relancer_agents.sh" 2>/dev/null
VIVANTS=$(for i in 00 01 02 03 04 05 06 07; do pgrep -f "agent${i}_loop" >/dev/null && echo 1; done | wc -l)
if [ "$VIVANTS" -lt 8 ]; then
  bash ~/relancer_agents.sh </dev/null >/tmp/relance.log 2>&1
fi
pgrep -f "aitif-fond.sh" >/dev/null || (nohup bash ~/aitif-fond.sh >/tmp/fond.log 2>&1 & disown)
echo "AITIF - $(date +%d-%m-%Y_%H:%M) - 8/8 vivants - Base prete"
bash ~/aitif-base.sh 2>/dev/null | head -12

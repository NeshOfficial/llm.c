#options = subprocess.check_output(["modprobe", "-c", "nvidia"], text=True)
#an_profile = len([l for l in options.splitlines() if "NVreg_RestrictProfilingToAdminUsers=0" in l]) != 0

# record metrics
# --full and --import-source are entirely superfluous for this script, but you might want to
# manually inspect `profile.ncu-rep`, so we keep it here
cmd = [ "--set", "full", "--import-source", "yes", "-o", "profile", "-f", "./profile_gpt2cu"]
# # do we need to run under sudo
# if not can_profile:
#     print("NVreg_RestrictProfilingToAdminUsers=1, running with sudo")
#     cmd = ["sudo"] + cmd
# subprocess.check_call(cmd)

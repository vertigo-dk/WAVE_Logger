#!/usr/bin/env python

def main():
    # Main loop / OSC Listener
    port = 7282
    ip = "127.0.0.1"

    #receiving osc
    import argparse
    from pythonosc import dispatcher
    from pythonosc import osc_server

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default=ip, help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=port, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/log", log)

    # serving forever
    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()

def log(unused_addr,input):
    import keen, time

    keen.project_id = "5880ce078db53dfda8a83dd1"
    keen.write_key = "B14E6F58BB99105E1A6784E3E73F366BFAFBC67A207195AB1394B1D514F73E08F81B2614B4CA079516B02CC3BDDFC24B8161AE1E1E9156BA7BAABD112F4963D52526CE07C27EADDF61CAF55057F8EB7A9D3CB04B2E24F5DADA5B82F990FFDD51"
    keen.read_key = "1CF1CD4E71C393FAFDA14BD8C0547B0F1C371D2D8534FACC4C5995F5D0AC8353D236277CFBD107E3674E2482169E0BA764FC3D76CD28D36D01E302A188432B7BA61C559B8D6ABEEE4BA4B9918833C5BA6099D85EAD5367C56BA6F374BEAA8347"

    import json
    keen_output = json.loads(input)

    keen.add_event("treeDataLog", keen_output)
    print("Log seent to Keen.io at: ", time.strftime('%X %x'))

if __name__ == "__main__":
    main()

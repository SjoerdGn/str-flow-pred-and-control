import neat
from .value_curves import translation_curve, penalty_curve_low_discharge
import numpy as np
import datetime as dt

generation = 0


def run_control(genomes, config, controller, riverdata, newsettingdates):
    # Init NEAT
    nets = []
    controls = []

    for id, g in genomes:
        net = neat.nn.FeedForwardNetwork.create(g, config)
        nets.append(net)
        g.fitness = 0

        # Init my cars
        controls.append(controller)


    # Main loop
    global generation
    generation += 1

    enum_nsd = iter(newsettingdates)
    ind = next(enum_nsd)

    while True:
        
        # Input my data and get result from network
        lev_r = riverdata['level'][ind]
        disch_pred = riverdata['discharge_pred'][ind]



        for i, control in enumerate(controls):
            output = nets[i].activate([lev_r, disch_pred])
            
            #print(f"Output: {output}")
            out_1, out_2 = output
            wl_1 = translation_curve(out_1, 1., 9., in_min=-1., in_max=1.)
            dis_2 = translation_curve(out_2, 0., 50., in_min=-1., in_max=1.)

            # TODO: kill really bad control 
            level_input = riverdata['level'][ind:ind+dt.timedelta(days=14)].values
            disch_input = riverdata['discharge'][ind:ind+dt.timedelta(days=14)].values
            value = control.return_total_value(
                                    level_input,
                                    disch_input,
                                    [None, dis_2*np.ones_like(level_input)],
                                    [wl_1*np.ones_like(level_input), None],
                                    penalty_curve_low_discharge)
           
            genomes[i][1].fitness += value

        ind = next(enum_nsd)
        if ind == newsettingdates[-1]:
            break
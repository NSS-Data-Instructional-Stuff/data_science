import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.cm import viridis
from sklearn.tree import DecisionTreeRegressor

def decision_tree_plot(X, y, dt):
    cm = viridis
    
    fig, ax = plt.subplots(figsize = (10,8))
    
    for i in range(len(dt.tree_.feature)):
        orient = dt.tree_.feature[i]
        th = dt.tree_.threshold[i]
        if orient == 0:
            ymin = 0
            ymax = 1
            while i in dt.tree_.children_left or i in dt.tree_.children_right:
                if i in dt.tree_.children_left:
                    idx = list(dt.tree_.children_left).index(i)
                    if orient != dt.tree_.feature[idx]:
                        ymax = min(ymax,dt.tree_.threshold[idx])
                    i = idx
                else:
                    idx = list(dt.tree_.children_right).index(i)
                    if orient != dt.tree_.feature[idx]:
                        ymin = max(ymin,dt.tree_.threshold[idx])
                    i = idx
            plt.vlines(x = th, ymin = ymin, ymax = ymax)
        elif orient == 1:
            xmin = 0
            xmax = 1
            while i in dt.tree_.children_left or i in dt.tree_.children_right:
                if i in dt.tree_.children_left:
                    idx = list(dt.tree_.children_left).index(i)
                    if orient != dt.tree_.feature[idx]:
                        xmax = min(xmax,dt.tree_.threshold[idx])
                    i = idx
                else:
                    idx = list(dt.tree_.children_right).index(i)
                    if orient != dt.tree_.feature[idx]:
                        xmin = max(xmin,dt.tree_.threshold[idx])
                    i = idx
            plt.hlines(y = th, xmin = xmin, xmax = xmax)
        elif orient == -2:
            val = dt.tree_.value[i]
            xmin, xmax = 0, 1
            ymin, ymax = 0, 1
            while i in dt.tree_.children_left or i in dt.tree_.children_right:
                if i in dt.tree_.children_left:
                    idx = list(dt.tree_.children_left).index(i)
                    if dt.tree_.feature[idx] == 0:
                        xmax = min(xmax,dt.tree_.threshold[idx])
                    else:
                        ymax = min(ymax,dt.tree_.threshold[idx])
                    i = idx
                else:
                    idx = list(dt.tree_.children_right).index(i)
                    if dt.tree_.feature[idx] == 0:
                        xmin = max(xmin, dt.tree_.threshold[idx])
                    else:
                        ymin = max(ymin, dt.tree_.threshold[idx])
                    i = idx
            rect = Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, 
                             linewidth=0, edgecolor='black', facecolor = cm((val[0][0] + 2) / 4))
            ax.add_patch(rect)

    plt.scatter(X[:,0], X[:,1], edgecolor = 'white', linewidth = 2,
                s = 100, c = y, cmap = cm, zorder = 100);

    plt.colorbar()    

    plt.xlim(0,1)
    plt.ylim(0,1);
    
def decision_tree_widget(X, y, max_depth = 1, show_prediction = False, show_breaks = False):
    fig, ax = plt.subplots(figsize = (10,8))
    
    dt = DecisionTreeRegressor(random_state = 321)
    dt.fit(X, y)
    
    # Now, prune down to the max_depth
    if max_depth:
        n_nodes = dt.tree_.node_count
        children_left = dt.tree_.children_left
        children_right = dt.tree_.children_right
        features = dt.tree_.feature
        
        node_depth = np.zeros(shape=n_nodes, dtype=np.int64)
        is_leaves = np.zeros(shape=n_nodes, dtype=bool)
        stack = [(0, 0)]  # start with the root node id (0) and its depth (0)
        while len(stack) > 0:
            # `pop` ensures each node is only visited once
            node_id, depth = stack.pop()
            node_depth[node_id] = depth

            # If the left and right child of a node is not the same we have a split
            # node
            is_split_node = children_left[node_id] != children_right[node_id]
            # If a split node, append left and right children and depth to `stack`
            # so we can loop through them
            if is_split_node:
                stack.append((children_left[node_id], depth + 1))
                stack.append((children_right[node_id], depth + 1))
            else:
                is_leaves[node_id] = True
                
        pruned_features = []
        for depth, feature in zip(node_depth, features):
            if depth == max_depth:
                feature = -2
            elif depth > max_depth:
                feature = -999     # This ensures that it does not draw a rectangle for this node.
            pruned_features.append(feature)
        pruned_features = np.array(pruned_features)
    else:
        pruned_features = dt.tree_.feature 
    
    
    cm = viridis

    if show_breaks:
        for i in range(len(dt.tree_.feature)):
            orient = pruned_features[i]
            th = dt.tree_.threshold[i]
            if orient == 0:
                ymin = 0
                ymax = 1
                while i in dt.tree_.children_left or i in dt.tree_.children_right:
                    if i in dt.tree_.children_left:
                        idx = list(dt.tree_.children_left).index(i)
                        if orient != dt.tree_.feature[idx]:
                            ymax = min(ymax,dt.tree_.threshold[idx])
                        i = idx
                    else:
                        idx = list(dt.tree_.children_right).index(i)
                        if orient != dt.tree_.feature[idx]:
                            ymin = max(ymin,dt.tree_.threshold[idx])
                        i = idx
                plt.vlines(x = th, ymin = ymin, ymax = ymax)
            elif orient == 1:
                xmin = 0
                xmax = 1
                while i in dt.tree_.children_left or i in dt.tree_.children_right:
                    if i in dt.tree_.children_left:
                        idx = list(dt.tree_.children_left).index(i)
                        if orient != dt.tree_.feature[idx]:
                            xmax = min(xmax,dt.tree_.threshold[idx])
                        i = idx
                    else:
                        idx = list(dt.tree_.children_right).index(i)
                        if orient != dt.tree_.feature[idx]:
                            xmin = max(xmin,dt.tree_.threshold[idx])
                        i = idx
                plt.hlines(y = th, xmin = xmin, xmax = xmax)
            elif orient == -2:
                val = dt.tree_.value[i]
                xmin, xmax = 0, 1
                ymin, ymax = 0, 1
                while i in dt.tree_.children_left or i in dt.tree_.children_right:
                    if i in dt.tree_.children_left:
                        idx = list(dt.tree_.children_left).index(i)
                        if dt.tree_.feature[idx] == 0:
                            xmax = min(xmax,dt.tree_.threshold[idx])
                        else:
                            ymax = min(ymax,dt.tree_.threshold[idx])
                        i = idx
                    else:
                        idx = list(dt.tree_.children_right).index(i)
                        if dt.tree_.feature[idx] == 0:
                            xmin = max(xmin, dt.tree_.threshold[idx])
                        else:
                            ymin = max(ymin, dt.tree_.threshold[idx])
                        i = idx
                rect = Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, 
                                 linewidth=0, edgecolor='black', facecolor = cm((val[0][0] + 2) / 4))
                if show_prediction:
                    ax.add_patch(rect)

    plt.scatter(X[:,0], X[:,1], edgecolor = 'white', linewidth = 2,
                s = 100, c = y, cmap = cm, zorder = 100);

    plt.colorbar()
    
    plt.xlim(0,1)
    plt.ylim(0,1);


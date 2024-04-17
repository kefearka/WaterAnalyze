from ClassApp import Application

__version__ = "0.0.1"

if __name__ == '__main__':
    # import numpy as np
    # import pandas as pd
    # import matplotlib as mpl
    # from platform import python_version
    # import tkinter as tk

    # print(f"Compile/Used components:\n"
    #       f"Python\t\t3.10.0 / {python_version()}\n"
    #       f"Tkinter\t\t8.6 / {str(tk.TkVersion)}\n"
    #       f"PANDAS\t\t1.5.1 / {pd.__version__}\n"
    #       f"NUMPY\t\t1.23.4 / {np.__version__}\n"
    #       f"MATPLOTLIB\t3.6.2 / {mpl.__version__}")

    app = Application()
    app.exec()
#####from class main windows
        # rect = 0.1, 0.1, 0.8, 0.8
        # t = np.arange(0.01, 10.0, 0.01)
        # scale = 1.10

        # fig = plt.Figure()

        # canvas = FigureCanvasTkAgg(fig, self.graph_frame)

        # ax1 = fig.add_axes(rect)
        # ax1.plot(t, np.exp(t), 'b-')  # Put your speed/power plot here
        # ax1.set_xlabel('Speed (mph)', color='b')
        # ax1.set_ylabel('Power', color='b')

        # ax2 = fig.add_axes(rect, frameon=False)
        # ax2.yaxis.tick_right()
        # ax2.yaxis.set_label_position('right')
        # ax2.xaxis.tick_top()
        # ax2.xaxis.set_label_position('top')

        # ax2.plot(t, np.sin(2 * np.pi * t), 'r-')  # Put your speed/rotation plot here
        # ax2.set_xlabel('Speed (kmph)', color='r')
        # ax2.set_ylabel('Rotations', color='r')

        # zp = ClassGraph()
        # figZoom = zp.zoom_factory(ax1, base_scale=scale)
        # figPan = zp.pan_factory(ax1)
        # figZoom2 = zp.zoom_factory(ax2, base_scale=scale)
        # figPan2 = zp.pan_factory(ax2)
        # canvas._tkcanvas.pack(fill=tk.BOTH, expand=1)
#####

# print("https://fadeevlecturer.github.io/python_lectures/notebooks/visualization/matplotlib.html")
# ---------------------------------------------

# print()
# # ToolTip
#
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Step 1. Create a scatter chart
# x = np.random.rand(20)
# y = np.random.rand(20)
# colors = np.random.randint(1, 5, size=len(x))
# norm = plt.Normalize(1, 4)
# cmap = plt.cm.PiYG
#
# fig, ax = plt.subplots()
# scatter = plt.scatter(
#         x=x,
#         y=y,
#         c=colors,
#         s=100,
#         cmap=cmap,
#         norm=norm
#     )
#
# # Step 2. Create Annotation Object
# annotation = ax.annotate(
#         text='',
#         xy=(0, 0),
#         xytext=(15, 15), # distance from x, y
#         textcoords='offset points',
#         bbox={'boxstyle': 'round', 'fc': 'w'},
#         arrowprops={'arrowstyle': '->'}
#     )
# annotation.set_visible(False)
#
# # Step 3. Implement the hover event to display annotations
# def motion_hover(event):
#     annotation_visbility = annotation.get_visible()
#     if event.inaxes == ax:
#         is_contained, annotation_index = scatter.contains(event)
#         if is_contained:
#             data_point_location = scatter.get_offsets()[annotation_index['ind'][0]]
#             annotation.xy = data_point_location
#
#             text_label = '({0:.4f}, {0:.4f})'.format(data_point_location[0], data_point_location[1])
#             annotation.set_text(text_label)
#
#             annotation.get_bbox_patch().set_facecolor(cmap(norm(colors[annotation_index['ind'][0]])))
#             annotation.set_alpha(0.4)
#
#             annotation.set_visible(True)
#             fig.canvas.draw_idle()
#         else:
#             if annotation_visbility:
#                 annotation.set_visible(False)
#                 fig.canvas.draw_idle()
#
#
# fig.canvas.mpl_connect('motion_notify_event', motion_hover)
# plt.show()

# print()
# ZOOM
# from matplotlib.pyplot import figure, show
# import numpy
#
# class ZoomPan:
#     def __init__(self):
#         self.press = None
#         self.cur_xlim = None
#         self.cur_ylim = None
#         self.x0 = None
#         self.y0 = None
#         self.x1 = None
#         self.y1 = None
#         self.xpress = None
#         self.ypress = None
#
#
#     def zoom_factory(self, ax, base_scale = 2.):
#         def zoom(event):
#             cur_xlim = ax.get_xlim()
#             cur_ylim = ax.get_ylim()
#
#             xdata = event.xdata # get event x location
#             ydata = event.ydata # get event y location
#
#             if event.button == 'down':
#                 # deal with zoom in
#                 scale_factor = 1 / base_scale
#             elif event.button == 'up':
#                 # deal with zoom out
#                 scale_factor = base_scale
#             else:
#                 # deal with something that should never happen
#                 scale_factor = 1
#                 print(event.button)
#
#             new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
#             new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor
#
#             relx = (cur_xlim[1] - xdata)/(cur_xlim[1] - cur_xlim[0])
#             rely = (cur_ylim[1] - ydata)/(cur_ylim[1] - cur_ylim[0])
#
#             ax.set_xlim([xdata - new_width * (1-relx), xdata + new_width * (relx)])
#             ax.set_ylim([ydata - new_height * (1-rely), ydata + new_height * (rely)])
#             ax.figure.canvas.draw()
#
#         fig = ax.get_figure() # get the figure of interest
#         fig.canvas.mpl_connect('scroll_event', zoom)
#
#         return zoom
#
#     def pan_factory(self, ax):
#         def onPress(event):
#             if event.inaxes != ax: return
#             self.cur_xlim = ax.get_xlim()
#             self.cur_ylim = ax.get_ylim()
#             self.press = self.x0, self.y0, event.xdata, event.ydata
#             self.x0, self.y0, self.xpress, self.ypress = self.press
#
#         def onRelease(event):
#             self.press = None
#             ax.figure.canvas.draw()
#
#         def onMotion(event):
#             if self.press is None: return
#             if event.inaxes != ax: return
#             dx = event.xdata - self.xpress
#             dy = event.ydata - self.ypress
#             self.cur_xlim -= dx
#             self.cur_ylim -= dy
#             ax.set_xlim(self.cur_xlim)
#             ax.set_ylim(self.cur_ylim)
#
#             ax.figure.canvas.draw()
#
#         fig = ax.get_figure() # get the figure of interest
#
#         # attach the call back
#         fig.canvas.mpl_connect('button_press_event',onPress)
#         fig.canvas.mpl_connect('button_release_event',onRelease)
#         fig.canvas.mpl_connect('motion_notify_event',onMotion)
#
#         #return the function
#         return onMotion
#
#
# fig = figure()
#
# ax = fig.add_subplot(111, xlim=(0,1), ylim=(0,1), autoscale_on=False)
#
# ax.set_title('Click to zoom')
# x,y,s,c = numpy.random.rand(4,200)
# s *= 200
#
# ax.scatter(x,y,s,c)
# scale = 1.05
# zp = ZoomPan()
# figZoom = zp.zoom_factory(ax, base_scale = scale)
# figPan = zp.pan_factory(ax)
# show()

# print()
# import numpy as np
# import matplotlib.pyplot as plt
#
# # Fixing random state for reproducibility
# np.random.seed(19680801)
#
# # some random data
# x = np.random.randn(1000)
# y = np.random.randn(1000)
#
#
# def scatter_hist(x, y, ax, ax_histx, ax_histy):
#     # no labels
#     ax_histx.tick_params(axis="x", labelbottom=False)
#     ax_histy.tick_params(axis="y", labelleft=False)
#
#     # the scatter plot:
#     ax.scatter(x, y)
#
#     # now determine nice limits by hand:
#     binwidth = 0.25
#     xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
#     lim = (int(xymax/binwidth) + 1) * binwidth
#
#     bins = np.arange(-lim, lim + binwidth, binwidth)
#     ax_histx.hist(x, bins=bins)
#     ax_histy.hist(y, bins=bins, orientation='horizontal')
#
#
# # start with a square Figure
# fig = plt.figure(figsize=(10, 10))
#
# # Add a gridspec with two rows and two columns and a ratio of 2 to 7 between
# # the size of the marginal axes and the main axes in both directions.
# # Also adjust the subplot parameters for a square plot.
# gs = fig.add_gridspec(2, 2,  width_ratios=(7, 2), height_ratios=(2, 7),
#                       left=0.1, right=0.9, bottom=0.1, top=0.9,
#                       wspace=0.05, hspace=0.05)
#
# ax = fig.add_subplot(gs[1, 0])
# ax_histx = fig.add_subplot(gs[0, 0], sharex=ax)
# ax_histy = fig.add_subplot(gs[1, 1], sharey=ax)
#
# # use the previously defined function
# scatter_hist(x, y, ax, ax_histx, ax_histy)
#
# plt.show()

import jinja2, sys, yaml

env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))

# recursivo no yaml
config = yaml.load(open(sys.argv[1], "r"), Loader=yaml.Loader)
template = env.get_template(sys.argv[1])
rendered = template.render(config)

# final
config = yaml.load(rendered, Loader=yaml.Loader)
template = env.get_template(sys.argv[2])
rendered = template.render(config)

print(rendered)
